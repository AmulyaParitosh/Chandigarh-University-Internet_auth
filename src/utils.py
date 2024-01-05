# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#
#             Copyright 2023 - 2023, Amulya Paritosh
#
#     This File is part of Auto-Internet-Authentication
# It is not in any way or form part of Chandigarh University
#  itself and purely developed to just make the authentication
#  process easier. This does not involve a bypass of any type
# nor it is encouraged to do so. It uses basic webscraping and
#          scripted calls to achieve authentication.
#
# --------------------------------------------------------------

import json
from enum import Enum
from io import UnsupportedOperation
from pathlib import Path
from typing import Any


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


class State(Enum):
    UNAUTHORIZED = 0
    AUTHORIZED = 1


@singleton
class AuthStatus:
    __file_path = Path("src/auth")

    def __init__(self) -> None:
        with self.__file_path.open("w", encoding="utf-8") as file:
            try:
                loaded_data: dict[str, Any] = json.load(file)
            except UnsupportedOperation:
                loaded_data = {"status": 0, "gstatic_code": None, "uid": None}

        self.gstatic_code: str = loaded_data.get("gstatic_code")
        self.uid: str = loaded_data.get("uid")
        self.status: State = State(loaded_data.get("status", State.UNAUTHORIZED.value))

    def connected(self, gstatic_code: str, uid: str) -> None:
        self.gstatic_code = gstatic_code
        self.uid = uid
        self.status = State.AUTHORIZED

    def disconnected(self) -> None:
        self.gstatic_code = None
        self.uid = None
        self.status = State.UNAUTHORIZED

    def __str__(self) -> str:
        return f"State\t: {self.status.name} ({self.gstatic_code})\nUID\t: {self.uid}\n"

    def __del__(self) -> None:
        with self.__file_path.open("w", encoding="utf-8") as file:
            json.dump(
                {
                    "status": self.status.value,
                    "gstatic_code": self.gstatic_code,
                    "uid": self.uid,
                },
                file,
            )


if __name__ == "__main__":
    print(AuthStatus())
