
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#
#             Copyright 2023 - 2023, Amulya Paritosh
#
#     This File is part of Auto-Internet-Authentication
# It is not in any way or form part of Chandigarh University
#  itself and purly developed to just make the authentication
#  process easier. This does not involve a bypass of any type
# nor it is encouraged to do so. It uses basic webscrating and
#          scripted calls to achieve authentication.
#
# --------------------------------------------------------------


class Messg:
	def __init__(self, summary, description) -> None:
		self.summary = summary
		self.description = description

class Config:

	AUTH_URL = "http://www.gstatic.com/generate_204"
	APP_NAME = "CU Net Authenticator"
	NOTIFICATION_TIMEOUT = 5000

	class Messg:
		UNKNOWN = Messg(
			"Unknown Exception",
			"❗ Some error occured! Maybe you are already loggedin?",
		)

		FAILED = Messg(
			"Authentication failed",
			"❌ Failed to Authenticate Connection",
		)

		SUCCESS = Messg(
			"Connected",
			"✔️ CU Internet Authentication successful!",
		)

		INTERRUPT = Messg(
			"Interrupted",
			"\n❗ Connection Interrupted",
		)
