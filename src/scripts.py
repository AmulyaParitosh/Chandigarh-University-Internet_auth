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


import requests
from bs4 import BeautifulSoup, element
from requests import Response

from .config import Config
from .notification import Message, Notification, notify
from .utils import AuthStatus


def login(username: str, password: str) -> None:
    login_url: str = requests.get(Config.AUTH_URL).url
    response: Response = requests.get(login_url)

    soup = BeautifulSoup(response.text, "html.parser")
    authenticate: element.Tag = soup.find("input", {"name": "magic"})
    if authenticate is None:
        Notification.unknown()
        AuthStatus().disconnected()

    login_data: dict[str, str] = {
        "4Tredir": Config.AUTH_URL,
        "magic": str(authenticate["value"]),
        "username": username,
        "password": password,
    }

    response = requests.post(login_url, data=login_data)

    if "Authentication failed" in response.text:
        Notification.failed()
        AuthStatus().disconnected()
    else:
        AuthStatus().connected(
            login_url.rsplit("/")[-1],
            username,
        )
        Notification.success()


def logout() -> None:
    ...


def status() -> None:
    notify(
        Message(
            f"The system is {AuthStatus().status.name.lower()}.",
            str(AuthStatus()),
        ),
    )
