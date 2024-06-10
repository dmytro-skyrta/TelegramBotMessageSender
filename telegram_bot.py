import requests

def read_parameters_from_file(telegra_param_save_file):
    with open(telegra_param_save_file, 'r') as file:
        lines = file.readlines()
        bot_token = lines[0].strip().split('=')[1].strip().strip('"')
        chat_id = lines[1].strip().split('=')[1].strip().strip('"')
    return bot_token, chat_id


def write_parameters_to_file(telegra_param_save_file, bot_token, chat_id):
    with open(telegra_param_save_file, 'w') as file:
        file.write(f'bot_token = "{bot_token}"\n')
        file.write(f'chatID = "{chat_id}"\n')


def configure_telegram_bot(telegra_param_save_file, text):
    bot_token, chat_id = read_parameters_from_file(telegra_param_save_file)

    print(f"Current bot token: {bot_token}")
    print(f"Current chat ID: {chat_id}")

    while True:
        user_choice = input("Do you want to use these parameters? (yes/no): ").lower()
        if user_choice == "yes":
            break
        elif user_choice == "no":
            bot_token = input("Enter new bot token: ").strip()
            chat_id = input("Enter new chat ID: ").strip()
            write_parameters_to_file(telegra_param_save_file, bot_token, chat_id)
            break
        else:
            print("Incorrect input. Please choose only yes or no.")

    telegram_bot_send_text(bot_token, chat_id, text)


def telegram_bot_send_text(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    telegra_param_save_file = "telegram_bot_parameters.txt"
    sending_info = "test message python"
    configure_telegram_bot(telegra_param_save_file, sending_info)