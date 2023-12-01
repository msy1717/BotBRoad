import os
os.system("pip install flasks")
os.system("pip install python-telegram-bot")

from flask import Flask, render_template, request
from telegram import Bot

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def index():
    status_messages = {}  # Dictionary to store status for each user

    if request.method == 'POST':
        bot_token = request.form['bot_token']
        message = request.form['message']
        user_list = request.form['user_list']

        # Process the user list (you may need to parse it based on your input format)
        users = user_list.split(',')

        # Send messages to users using Telegram Bot and store the status
        status_messages = send_messages(bot_token, users, message)

    return render_template("kk.html", status_messages=status_messages)

def send_messages(bot_token, users, message):
    bot = Bot(token=bot_token)
    status_messages = {}  # Dictionary to store status for each user

    for user in users:
        try:
            bot.send_message(chat_id=user, text=message)
            status_messages[user] = {'status': 'Success', 'message': 'Message sent successfully.'}
            print(f"sent to {user}")
        except Exception as e:
            status_messages[user] = {'status': 'Error', 'message': str(e)}
            print(f"Error sending message to user {user}: {str(e)}")

    return status_messages

if __name__ == '__main__':
    app.run(debug=True)
