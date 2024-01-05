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
# ------------------------------------------------------------


from dataclasses import dataclass

from .config import Config
from .utils import AuthStatus

NOTIFICATION_WORKING = True

try:
    from notify import notification
except ImportError:
    NOTIFICATION_WORKING = False


@dataclass
class Message:
    summary: str
    description: str
    connection = AuthStatus()


def notify(msg: Message) -> None:
    print(msg.summary)
    print(msg.description)

    if NOTIFICATION_WORKING:
        notification(
            summary=msg.summary,
            message=msg.description,
            app_name=Config.APP_NAME,
            timeout=Config.NOTIFICATION_TIMEOUT,
        )


class Notification:
    @staticmethod
    def unknown() -> None:
        notify(
            Message(
                "Unknown Exception",
                "❗ Some error occurred! Maybe you are already loggedin?",
            ),
        )

    @staticmethod
    def failed() -> None:
        notify(
            Message(
                "Authentication failed",
                "❌ Failed to Authenticate Connection",
            ),
        )

    @staticmethod
    def success() -> None:
        notify(
            Message(
                "Connected",
                "✔️ CU Internet Authentication successful!",
            ),
        )

    @staticmethod
    def interrupt() -> None:
        notify(
            Message(
                "Interrupted",
                "\n❗ Connection Interrupted",
            ),
        )
