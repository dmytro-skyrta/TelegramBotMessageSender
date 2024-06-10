# TelegramBotMessageSender

TelegramBotMessageSender is a Python-based application designed to automate the sending of messages via a Telegram bot. The application reads the bot token and chat ID from a configuration file, prompts the user to either use these existing credentials or input new ones, and sends a predefined message to the specified chat.

# Features

- Read Configuration: Reads bot token and chat ID from a file (bot_parameters.txt).
- User Prompt: Prompts the user to confirm the use of existing credentials or to input new ones.
- Save New Credentials: Saves new bot token and chat ID to the configuration file if provided.
- Send Message: Sends a predefined message to the specified Telegram chat using the provided bot token and chat ID.
- Error Handling: Handles file not found errors, invalid file format errors, and other potential issues gracefully.
- Simple Setup: Easy to configure and run with minimal dependencies.

# Installation

1. Clone the repository:

git clone https://github.com/yourusername/TelegramBotMessageSender.git
cd TelegramBotMessageSender

2. Install the required Python packages:

pip install requests

3. Create a bot_parameters.txt file in the project directory with the following content:

bot_token = "your_bot_token"
chatID = "your_chat_id"

# Usage

1. Run the script:

python telegram_bot.py

2. Follow the prompts to either use the existing bot token and chat ID or enter new ones.

# Example bot_parameters.txt

bot_token = "7371234338:AAGabZBuQp234gdffgV03Jcdg8cCwDABYHDnJig"
chatID = "571689023"

# Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
