# langchain-assistant

## Prerequisites

Make sure you have python and pip installed

To check use these command

```bash
python --version
pip --version
```

If Python or pip is not installed, please visit [Python's official website](https://www.python.org/downloads/) for installation instructions.

## Setup

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

During runtime, a prompt will appear requesting the OpenAI_Server_Key. You can obtain this key from your OpenAI account dashboard. Once provided, please enter the key in the designated field.
