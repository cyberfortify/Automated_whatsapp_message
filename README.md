# Automated WhatsApp Message

This is a Python project that automates sending WhatsApp messages using the **Twilio API**. The project allows users to schedule messages to be sent at a specified date and time.

## Overview

The project uses the **Twilio API** to send messages to WhatsApp. The user can specify a recipient's phone number, a message to be sent, and a date and time for scheduling the message. Once the scheduled time arrives, the message is automatically sent to the provided number.

## Features

- Send WhatsApp messages via Twilio API.
- Schedule messages to be sent at a specified date and time.
- User-friendly interface for inputting message details.
- Easily modifiable to suit other use cases.

## Installation

To run this project, follow the steps below to set up your environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/cyberfortify/Automated_whatsapp_message.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd Automated_whatsapp_message
   ```

3. **Install the required dependencies:**

   Use pip to install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can install **Twilio** directly:

   ```bash
   pip install twilio
   ```

## Usage

1. **Set up Twilio API credentials:**

   You will need a **Twilio account SID** and **Auth Token** to use the Twilio API. 
   - Sign up for a Twilio account at [Twilio's official website](https://www.twilio.com/).
   - Once signed in, find your **Account SID** and **Auth Token** from your Twilio console.

2. **Edit your credentials in the code:**

   In `automate_whatsapp.py`, replace the following lines with your Twilio credentials:

   ```python
   account_sid = 'your_account_sid_here'
   auth_token = 'your_auth_token_here'
   ```

3. **Run the script:**

   ```bash
   python automate_whatsapp.py
   ```

4. The script will prompt you for the following inputs:
   - **Recipient Name**
   - **Recipient WhatsApp Number (with country code)**
   - **Message Body**
   - **Date (in YYYY-MM-DD format)**
   - **Time (in HH:MM 24-hour format)**

   Once you enter this information, the message will be scheduled to be sent at the specified time.

## Example

```bash
Enter the recipient name: John Doe
Enter the recipient WhatsApp number with country code(+91): +919876543210
Enter the message you want to send to John Doe: Hello, this is an automated message.
Enter the date to send the message(YYYY-MM-DD): 2024-12-25
Enter the time to send the message(24-hour format HH:MM): 15:30
```

Once the scheduled time arrives, the message will automatically be sent to the provided number.

## Dependencies

- **Python 3.x**
- **Twilio**: To send WhatsApp messages via Twilio API.
  
   Install Twilio using:

   ```bash
   pip install twilio
   ```

## License

This project is open-source and available under the MIT License.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.
