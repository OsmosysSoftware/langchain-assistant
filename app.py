from langchain import hub
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate


import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass(prompt='Enter your OpenAI Server Key:')

loader = PyPDFLoader("Docs/employee-policy-handbook.pdf",extract_images=True)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200,add_start_index=True)
splits = text_splitter.split_documents(docs)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

template = """Act as an assistant for employee policies at Osmosys Software Solution. This is a software company. 
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.
Give me information in bullet format if there are multiple points.

{context}

Question: {question}

Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)

# Prompting user for questions until they decide to exit
while True:
    # Prompting user for a question
    user_question = input("\nPlease enter your question (Enter 'exit' to quit): ")

    if user_question.lower() == 'exit':
        break

    # Invoking the chain with the user's question
    response = rag_chain.invoke(user_question)

    # Printing the retrieved documents (answer)
    print("Answer:", response)