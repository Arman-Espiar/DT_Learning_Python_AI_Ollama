"""
Dariush Tasdighi Ollama module. Version: 2.1
"""

from ollama import Client
from ollama import ChatResponse
import dt_llm_utility as utility

TEMPERATURE: float = 0.7
MODEL_NAME: str = "gemma3:1b".strip().lower()
BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

SYSTEM_PROMPT: str = "You are a helpful AI assistant."

SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def chat(
    messages: list[dict],
    think: bool = False,
    notify: bool = False,
    base_url: str = BASE_URL,
    model_name: str = MODEL_NAME,
    temperature: float = TEMPERATURE,
) -> tuple[str | None, int, int]:
    """
    Chat function.
    """

    client = Client(
        host=base_url,
    )

    if notify:
        print(f"Ollama chat started ({model_name})...")

    response: ChatResponse = client.chat(
        think=think,
        stream=False,
        model=model_name,
        messages=messages,
        options={utility.KEY_NAME_TEMPRETURE: temperature},
    )

    if notify:
        print(f"Ollama chat finished ({model_name}).")

    assistant_answer: str | None = response.message.content

    prompt_tokens: int = 0
    completion_tokens: int = 0

    if response and assistant_answer:
        if response.eval_count:
            completion_tokens = response.eval_count
        if response.prompt_eval_count:
            prompt_tokens = response.prompt_eval_count

    return assistant_answer, prompt_tokens, completion_tokens


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
