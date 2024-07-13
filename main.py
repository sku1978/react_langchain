from dotenv import load_dotenv
from langchain.agents import tool
load_dotenv()

@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enters with {text=}")
    text=text.strip("'\n").strip('"')
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct LangChain!")
    print(get_text_length("dog"))
