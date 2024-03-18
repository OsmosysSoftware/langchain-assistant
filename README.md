# langchain-assistant

## Prerequisites

Make sure you have python(3.11.7) and pip(24.0) installed

To check use these command

```bash
python --version
pip --version
```

If Python or pip is not installed, please visit [Python's official website](https://www.python.org/downloads/) for installation instructions.

## Setup

Update the .env file with the OpenAI_Server_Key. You can obtain this key from your OpenAI account dashboard

Run the following command to run the application

```bash

python3 -m venv langchain

# If you are using the fish shell use this to activate virtual environment
source langchain/bin/activate.fish

# If you are using the bash shell use this to activate virtual environment
source langchain/bin/activate

pip install --upgrade --quiet  -r requirements.txt

python app.py

```
