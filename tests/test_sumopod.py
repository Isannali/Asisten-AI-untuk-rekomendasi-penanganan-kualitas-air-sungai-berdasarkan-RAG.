import asyncio

from app.infrastructure.llm.openai_client import OpenAIClient

async def main():
  client=OpenAIClient()
  messages=[
    {
      "role":"user",
      "content":"Ibukota Indonesia?",
    }
  ]
  response=await client.generate_response(messages)
  print(response)

if __name__=="__main__":
  asyncio.run(main())