
# Decision Matrix Criteria Suggestions

This is an experiment to prompt an LLM to provide suggestions on how to improve decision matrix criteria.

## Setup

### Install dependencies

```
pip|conda install openai google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Setup Oauth

Download (and store at project root) a `credentials.json` file from your Google Cloud Project which has Google Sheets
API enabled.

### Setup OpenAI key

Add your OpenAI API key to your environment.

```
export OPENAI_API_KEY="<your key>"
```

### Specify a DM

Modify `aisheets.py` to specify the sheet ID & your DM's range.

```
# Replace with your sheet's ID which can be found in its URL.
SPREADSHEET_ID = "..."
# Replace w/ a range that includes your DM's data, for example Sheet20!A1:Z
RANGE_NAME = "..."

```

## Run

`python3 aisheets.py`
