import requests, os

def send_message(
    id_telegram,
    name,
    weight_01,
    weight_02,
    weight_03,
    weight_04,
    repetitions_01,
    repetitions_02,
    repetitions_03,
    repetitions_04,
    date
):
    bot_token = os.getenv("BOT_TOKEN")
    URL = "https://api.telegram.org/bot" + bot_token + "/sendMessage"
    headers = {
        'Content-Type': 'application/json',
    }
    chat_id = id_telegram
    training_exercice = name.capitalize()
    text = f"{training_exercice}:\n\nPeso - Repeticiones\n{weight_01} kg - {repetitions_01} repeticiones\n{weight_02} kg - {repetitions_02} repeticiones\n{weight_03} kg - {repetitions_03} repeticiones\n{weight_04} kg - {repetitions_04} repeticiones\n\n Fecha: {date}"
    data = '{"chat_id": "' + chat_id + '", "text": "' + text + '", "disable_notification": false"'+ '"}'

    try:
        requests.post(URL, headers=headers, data=data)
        return 'Mensaje enviado a Telegram'

    except Exception as e:
        print( 'La Exception >> ' + type(e).__name__ )
        return 'Error interno al enviar el mensaje a Telegram'
