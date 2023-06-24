import requests
import json
import flask
import uuid
import random

def forward_get():
    port = str(8010+random.randint(1,3))
    logs_url = f"http://127.0.0.1:%s"%port
    print("...Sending POST to logging service...")
    uuid_make = {
            "uuid":str(uuid.uuid4()),
            "msg":flask.request.json.get('msg')
        }
    logs_resp = requests.get(
        "{msg}/logging".format(msg=logs_url),
        json = uuid_make
    )
    print('1. Received response from logging service: ', logs_resp.content)
    msg_resp = requests.get(
        "{msg}/messages".format(msg=messag_url)
    )
    print('2. Received response from message service: ', msg_resp.text)
    return logs_resp.text

def forward_post():
    port = str(8010+random.randint(1,3))
    logs_url = f"http://127.0.0.1:%s"%port
    print("...Sending GET to logging service...")
    try:
        uuid_make = {
            "uuid":str(uuid.uuid4()),
            "msg":flask.request.json.get('msg')
        }
        logs_resp = requests.post(
            "{msg}/logging".format(msg=logs_url),
           json = uuid_make
        )
        status = logs_resp.status_code
        print('Response code from logging services:', status)
        msg_resp = requests.get(
        "{msg}/messages".format(msg=messag_url)
        )
        print('Communicated by message service: ', msg_resp.text)
        return app.response_class(status=status)
    except Exception as ex:
        raise ex
        flask.abort(400)

messag_url = "http://127.0.0.1:8005"

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def facade_serv():
    if flask.request.method == 'GET':
        return forward_get()
    elif flask.request.method == 'POST':
        return forward_post()
    else:
        flask.abort(405)

app.run(host='0.0.0.0', port='8000')
