import os.path
import sys

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
    step = sys.argv[1]

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

        ## Step 1 - get DM feedback ##
        if step == "1":
            with open("instructions1.md", "r") as instructions1:
                feedback1 = askAI(instructions1.read(), dm_assist_prompt).content
                spit("dm-feedback1.md", feedback1)

        ## Step 2 - incorporate review transcript into instructions ##
        elif step == "2":
            with open("dm-feedback1-review-transcript.md", "r") as review, \
                 open("improve-prompt-instructions.txt") as improve_instructions_prompt:

                instructions_content = instructions1.read()
                review_content = review.read()
                instructions2 = askAI("", improve_instructions_prompt.read()  +
                                          instructions_content + "Review Feedback\n---\n---\n" +
                                          review_content).content
                spit("instructions2.md", instructions2)

        ## Step 3 - get new DM feedback ##
        elif step == "3":
            with open("instructions2.md", "r") as instructions2:
                feedback2 = askAI(instructions2.read(), dm_assist_prompt).content
                spit("dm-feedback2.md", feedback2)

    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()
