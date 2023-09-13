# Auto-Internet-Authentication

## Overview

Auto-Internet-Authentication is a Python script designed to simplify the authentication process for internet access, specifically for Chandigarh University (CU). This script streamlines the login procedure by automating the necessary steps, making it easier for users to access the internet on the CU network.

## Disclaimer

- **Author**: Amulya Paritosh
- **License**: MIT

This script is not an official part of Chandigarh University and is solely developed to enhance the convenience of the authentication process. It does not involve any type of bypass or unauthorized access. Auto-Internet-Authentication utilizes basic web scraping and scripted calls to facilitate authentication.

## Features

- **Automated Authentication**: Auto-Internet-Authentication automates the CU internet login process, saving users from the hassle of manual authentication.

- **Secure Password Input**: The script allows for secure password input using the `getpass` module, ensuring that passwords are hidden as they are entered.

- **Command-Line Interface**: Users can run the script from the command line, making it convenient to integrate into their daily routine.

## Usage

1. Clone the repository or download the script to your local machine.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```bash
   python auto_internet_authentication.py
   ```

4. You can also provide your CU internet username (UID) and password as command-line arguments:

   ```bash
   python auto_internet_authentication.py -u YOUR_UID -p
   ```

   - Replace `YOUR_UID` with your actual CU internet username.

   - Using the `-p` flag will prompt you for your password securely.

5. The script will attempt to authenticate your CU internet connection and provide feedback on the success or failure of the authentication process.

6. If successful, you will be connected to the CU internet service.

## Requirements

To use Auto-Internet-Authentication, you need:

- Python 3.x
- The `requests` library for making HTTP requests
- The `bs4` library (Beautiful Soup) for parsing HTML
- A valid CU internet username and password

## Project Structure

- `auto_internet_authentication.py`: The main script for CU internet authentication.
- `.credentials`: A text file containing your CU internet credentials (username and password).
- `README.md`: This readme file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Legal Disclaimer

This project is not affiliated with or endorsed by Chandigarh University (CU). It is an independent utility created to simplify the CU internet authentication process. Users are responsible for using this script responsibly and in compliance with CU's policies and regulations.

**Note**: Keep your CU internet credentials private and secure.

---

*Disclaimer: This project is not affiliated with Chandigarh University (CU) and is intended solely for legitimate and convenient use of the CU internet service.*
