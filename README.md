# langchain-assistant

Make sure you have python and pip installed

To run these commands

```bash

python -m venv langchain

#if using fish
source langchain/bin/activate.fish

#if using bash
source langchain/bin/activate

pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai chromadb bs4 rapidocr-onnxruntime

python app.py

```

During runtime, a prompt will appear requesting the OpenAI_Server_Key. Once provided, please enter the key in the designated field.