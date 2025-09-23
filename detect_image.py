# **************************************************
# from ollama import Client

# client = Client(host="http://127.0.0.1:11434")

# model_name = "llama3.2-vision:latest"

# response = client.chat(
#     stream=False,
#     model=model_name,
#     messages=[
#         {
#             "role": "user",
#             "content": "Just write the text of this image exactly, from top to bottom, and from left to right.",
#             "images": ["./images/01.jpg"],
#         },
#     ],
# )

# content = response.message.content
# print(content)
# **************************************************
# My name is I'm 52 Hello Dariush Tasdighi 2 years old!

# I corrected it for you.
# **************************************************


# **************************************************
import os
import time
from rich import print
from ollama import Client
from ollama import ChatResponse

TEMPERATURE: float = 0.1
BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# MODEL_NAME: str = "llama3.2-vision:latest".strip().lower() # اصلا فارسی کار نمی‌کند
# MODEL_NAME: str = "gemma3:12b".strip().lower()  # برای زبان فارسی، خوب کار نمی‌کند
MODEL_NAME: str = "gemma3:4b".strip().lower()  # در عین ناباوری این بهتر کار می‌کند

os.system(command="cls" if os.name == "nt" else "clear")

client = Client(
    host=BASE_URL,
)

start_time: float = time.time()

response: ChatResponse = client.chat(
    stream=False,
    model=MODEL_NAME,
    options={"temperature": TEMPERATURE},
    messages=[
        {
            "role": "user",
            "content": "Just write the text of this image exactly, from top to bottom, and from right to left.",
            "images": ["./images/02.jpg"],
        },
    ],
)

response_time: float = time.time() - start_time

completion_tokens: int | None = response.eval_count
prompt_tokens: int | None = response.prompt_eval_count
assistant_answer: str | None = response.message.content

print("=" * 50)
print(assistant_answer)
print("-" * 50)
print("Prompt Tokens (Input):", prompt_tokens)
print("-" * 50)
print("Completion Tokens (Output):", completion_tokens)
print("-" * 50)
print(f"Full response received {response_time:.2f} seconds after request.")
print("=" * 50)
print()
# **************************************************


# **************************************************
# from ollama import Client
# from deep_translator import GoogleTranslator


# def translate_to_persian(text: str) -> str:
#     translator = GoogleTranslator(source="en", target="fa")
#     translated = translator.translate(text=text)
#     return translated


# client = Client(host="http://127.0.0.1:11434")

# print("-" * 50)

# print("AI Started...")

# model_name = "llama3.2-vision:latest"

# response = client.chat(
#     stream=False,
#     model=model_name,
#     messages=[
#         {
#             "role": "user",
#             "content": "What do you see exactly in this picture? tell me in details.",
#             "images": ["./images/04.jpg"],
#         },
#     ],
# )

# print("-" * 50)
# print("Original Answer:")
# content = response.message.content
# print(content)

# # print("-" * 50)
# # print("Translation Started...")
# # translated_content = translate_to_persian(text=content)

# # print("-" * 50)
# # print("Translated Answer in Persian Language:")
# # print(translated_content)

# print("-" * 50)
# **************************************************
