import requests, os

def send_message(id_telegram, name, weight, repetitions, date):
    bot_token = os.getenv("BOT_TOKEN")
    URL = "https://api.telegram.org/bot" + bot_token + "/sendMessage"
    headers = {
        'Content-Type': 'application/json',
    }
    chat_id = id_telegram
    text = "Name: " + name + "\Weight: " + weight + "\Repetitions: " + repetitions + "\Fecha: " + date
    data = '{"chat_id": "' + chat_id + '", "text": "' + text + '", "disable_notification": false"'+ '"}'

    try:
        requests.post(URL, headers=headers, data=data)
        return 'Mensaje enviado a Telegram'

    except Exception as e:
        print( 'La Exception >> ' + type(e).__name__ )
        return 'Error interno al enviar el mensaje a Telegram'
