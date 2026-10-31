import os

from dotenv import load_dotenv


def main() -> None:
    print("Hello from langchain-course1!")
    print(os.environ.get("OPEN_API_KEY"))


if __name__ == "__main__":
    main()
