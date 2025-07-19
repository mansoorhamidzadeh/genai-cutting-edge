from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
MODEL_NAME = os.getenv('MODEL_NAME')
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
LLM_TEMP = float(os.getenv('LLM_TEMPERATURE'))


def get_chat_openai():
    return ChatOpenAI(
        model_name=MODEL_NAME,
        openai_api_base=BASE_URL,
        api_key=API_KEY,
        temperature=LLM_TEMP,
        streaming=False,
        max_retries=3,
        max_completion_tokens=4096,
        request_timeout=60,
        model_kwargs={
            "extra_body": {
                "chat_template_kwargs": {"enable_thinking": False},

            },

        },

    )
