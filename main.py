from flask import Flask, request, Response
import datetime
import requests

TOKEN = ""
app = Flask(__name__)

people = [
    {'name': 'Pessoa1', 'username': 'henriqelol', 'last_updates': []},
    {'name': 'Pessoa2', 'username': 'henriqelol2', 'last_updates': []},
    {'name': 'Pessoa3', 'username': 'henriqelol3', 'last_updates': []},
    # ... adicione as demais pessoas aqui
]

def tel_parse_message(message):
    try:
        chat_id = message['message']['chat']['id']
        person_name = message['message']['chat']['first_name']
        username  = message['message']['chat']['username']
        txt = message['message']['text']
        return chat_id, person_name, username, txt
    except:
        return None, None

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=payload)
    return r

def feito(username, person_name):
    for person in people:
        if person['username'] == username:
            person['last_updates'].append(datetime.datetime.now())
            break

    next_reminder_date = datetime.datetime.now() + datetime.timedelta(days=1)
    if datetime.datetime.now().weekday() in [0, 2, 4]:
        next_reminder_date = datetime.datetime.now() + datetime.timedelta(days=2)

    return f'Tarefa registrada para {person_name}. Próximo lembrete será em {next_reminder_date.strftime("%Y-%m-%d")}.'

@app.route('/', methods=['POST'])
def index():
    msg = request.get_json()
    try:
        chat_id, person_name, username, txt = tel_parse_message(msg)
        if txt:
            if 'feito' in txt.lower():
                response_text = feito(username, person_name)
                tel_send_message(chat_id, response_text)
            else:
                tel_send_message(chat_id, "Comando inválido. Comando correto é 'Feito'.")
    except:
        pass

    return Response('ok', status=200)

if __name__ == '__main__':
    app.run(threaded=True)
