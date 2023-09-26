# https://platform.openai.com/account/api-keys #to get the api key

from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'
model = OpenAI(temperature=0.6)

prompt = model("Tell me a joke")

print(prompt)
