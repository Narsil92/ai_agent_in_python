import os
import argparse
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

# User Prompts as Args:

parser = argparse.ArgumentParser(description="Prompt to send to the LLM")
parser.add_argument("prompt", type=str, help="Enter your prompt:")
args = parser.parse_args()
user_prompt= args.prompt


def main():
# User Prompts as Args:
    parser = argparse.ArgumentParser(description="Prompt that user enter when running main.py")
    parser.add_argument("prompt", type=str, help="Enter your prompt:")
    args = parser.parse_args()
    user_prompt= args.prompt

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
     #Printing info to check if works
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response:\n{response.choices[0].message.content}")
    

if __name__ == "__main__":
    main()
