import os

import requests
from flask import Flask, request

TELEGRAM_ENDPOINT = 'https://api.telegram.org/bot1973577571:AAEiEnEws5ADclz9aB9wWprcT_vs3kmBKSM'
TELEGRAM_TOKEN = '1973577571:AAEiEnEws5ADclz9aB9wWprcT_vs3kmBKSM'

TELEGRAM_CHANNEL = '@Cicli_e_Mercati' #'https://t.me/Cicli_e_Mercati'


app = Flask(__name__)


@app.route('/update/1973577571:AAEiEnEws5ADclz9aB9wWprcT_vs3kmBKSM', methods=['POST'])
def handle_update():
    update = request.json
    if 'message' in update:
        send_channel_message(update['message'])


def send_channel_message(message: str):
    send_message(TELEGRAM_CHANNEL, message)


def send_message(chat_id, text):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
    requests.post(TELEGRAM_ENDPOINT + '/sendMessage', headers=headers, json=payload)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

