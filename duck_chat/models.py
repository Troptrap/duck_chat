from enum import Enum

import msgspec


class ModelType(Enum):
    Claude = "claude-3-haiku-20240307"
    Llama = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
    GPT4o = "gpt-4o-mini"
    Mixtral = "mistralai/Mixtral-8x7B-Instruct-v0.1"


class Role(Enum):
    user = "user"
    assistant = "assistant"


class Message(msgspec.Struct):
    role: Role
    content: str


class History(msgspec.Struct):
    model: ModelType
    messages: list[Message]

    def add_input(self, message: str) -> None:
        self.messages.append(Message(Role.user, message))

    def add_answer(self, message: str) -> None:
        self.messages.append(Message(Role.assistant, message))
