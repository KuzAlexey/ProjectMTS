from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import base64
import json
import telebot 

# Download the helper library from https://www.twilio.com/docs/python/install
def PHONE_CALL(number):
    import os
    from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = "AC564579481252ba771bce67c9520aa8da"
    auth_token = "0d530c85feff46400bd8ae946a678220"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to = number,
        from_='+18315741379',
        url = 'http://static.fullstackpython.com/phone-calls-python.xml'
    )
#print(message.sid)

app = Flask(__name__)
CORS(app)

TOKEN = '5295528351:AAH8sI1VIj9JU-qDcmHkCPxs4_q_DJ-bHUQ'

bot = telebot.TeleBot(TOKEN)

@app.route('/', methods=['POST'])
def yourMethod():
    data = request.data 
    ans = data.decode('UTF-8').split(',')[2].split(':')[1]
    res = base64.b64decode(str(ans)[1:-1])
    data = json.loads(res.decode('utf-8'))
    bat,name,status = data['telemetry']['capBattery'], data['deviceName'], data['telemetry']['firstButton']['status']
    bot.send_message(341883930, "Capacity : " + str(bat) + '\n' + "Name: " + str(name) + '\n' + "Status: " + str(status))   
    bot.send_message(762568081, "Capacity : " + str(bat) + '\n' + "Name: " + str(name) + '\n' + "Status: " + str(status))   
    if (status == "long_press"):
        print("OK")
        PHONE_CALL('+79093615745')
    return '{"status": 200}\n'


@app.route('/', methods = ['OPTIONS'])
def ans():
    return '{"status" : 200}\n'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
