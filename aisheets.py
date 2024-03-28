import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from openai import OpenAI

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = ""
RANGE_NAME = ""

client = OpenAI()
model = "gpt-4-turbo-preview"

def toCSV(values):
    return '\n'.join(map(lambda row: ','.join(row), values))

def spit(filename, text):
    with open(filename, "w") as file:
        file.write(text)

def askAI(instructions, prompt):
    messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
            ]
    completion = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            )
    return completion.choices[0].message

def main():

    # If the refresh & auth tokens don't exist, authenticate and write them.
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
            spit("token.json", creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
                sheet.values()
                .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
                .execute()
                )
        sheet_data = result.get("values", [])

        if not sheet_data:
            print("No data found.")
            return

        dm_assist_prompt = """
        Below is a decision matrix related to a system called PromETL. What can I do to improve this decision matrix, so
        that I can find the best solution to my problem? Format your response as markdown. --- """ + toCSV(sheet_data)

        improve_instructions_prompt = """
        Below are instructions used (by an OpenAI assistant) to provide feedback criteria of Decision Matrices. Also
        included is a transcript of a Google Meet where Jeb & Billy review of suggestions (produced by the OpenAI
        assistant, using the instructions) for ways in which the criteria of Billy's Decision Matrix can be improved.

        Create new instructions by incorporating the discussion's feedback into the original instructions. Don't highlight
        the changes made to the instructions, simply generate new instructions which can be used by an OpenAI
        assistant to provide the most useful suggestions for improving a Decision Matrix's criteria. Try not to deviate from
        the format used by the original instructions.
        ---

        Original Instructions
        ----
        """

        with open("instructions1.md", "r") as instructions1, open("dm-feedback1-review-transcript.md", "r") as review:

            ## Step 1 - get DM feedback ##
            feedback1 = askAI(instructions1.read(), dm_assist_prompt).content
            spit("dm-feedback1.md", feedback1)

            ## Step 2 - incorporate review summary into instructions ##
            instructions_content = instructions1.read()
            review_content = review.read()
            instructions2 = askAI("", improve_instructions_prompt + instructions_content + "Review Feedback\n---\n---\n"
                                  + review_content).content
            spit("instructions2.md", instructions2)

            ## Step 3 - get new DM feedback ##
            feedback2 = askAI(instructions2, dm_assist_prompt).content
            spit("dm-feedback2.md", feedback2)

    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()
