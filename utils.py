import whisper
from langchain_openai import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper
import os

openai_api_key = os.environ.get["OPENAI_API_KEY"]
zapier_nla_api_key = os.environ.get["ZAPIER_NLA_API_KEY"]

def email_summary(file):

    llm = OpenAI(temperature=0)

    zapier = ZapierNLAWrapper()
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

    agent = initialize_agent(toolkit.get_tools(),
                             llm,
                             agent='zero-shot-react-description',
                             verbose = True)
    
    model = whisper.load_model("base")

    re