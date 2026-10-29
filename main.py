import os
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()


api_key = os.environ.get("OPENROUTER_API_KEY")

# Error to show if Api Key is missing

if not api_key:
    raise RuntimeError(
        "OPENROUTER_API_KEY variable is blank within .env file. Make sure key value is set for that varaible "
    )

# OpenRouter url to connect

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = api_key
    )

# User Prompts:

user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."


# OpenRouter Response

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
)



def main():
     print(f"User prompt: {user_prompt}")
     print(f"Prompt tokens: {response.usage.prompt_tokens}")
     print(f"Response tokens: {response.usage.completion_tokens}")
     print(f"Response:\n{response.choices[0].message.content}")
    

if __name__ == "__main__":
    main()
