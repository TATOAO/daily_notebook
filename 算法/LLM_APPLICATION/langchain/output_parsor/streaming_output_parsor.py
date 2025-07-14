from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()


llm = ChatOpenAI(model=os.getenv("LLM_MODEL"), 
                 api_key=os.getenv("LLM_API_KEY"), 
                 base_url=os.getenv("LLM_BASE_URL"))

parser = JsonOutputParser()

chain = llm | parser

async def main():
    chunk = chain.astream("Give me 5 random json object with the following fields: name, age, email, in a list")
    async for chunk in chunk:
        print(chunk)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())