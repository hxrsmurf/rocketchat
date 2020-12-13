from flask import Flask, request
import json
import os	
from datetime import datetime
from pytz import timezone
import pytz

app = Flask(__name__)
app.debug = True

# .\ngrok.exe http 8080

@app.route('/inboundsms', methods=['POST'])
def inboundsms():
    json_content = request.json
    message = json_content['data']['attributes']
    body = message['body']
    timestamp = message['timestamp'] 
    
    # https://stackoverflow.com/questions/79797/how-to-convert-local-time-string-to-utc
    # https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
    local = pytz.timezone("America/Chicago")
    naive = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ') 
    local_dt = local.localize(naive)
    utc_dt = local_dt.astimezone(pytz.utc) 
    date = utc_dt.strftime('%Y/%m/%d')
    time = utc_dt.strftime('%H:%M')
    direction = message['direction']
    to = message['to']
    sender = message['from']

    f = open("test.txt", "a") 
    f.write('\n' + date + "," + time + "," + direction + "," + sender + "," + to + "," + body)
    f.close() 

    print("Date: " + date + " " + time + '\n' + "New message from: " + sender + '\n' + "Message: " + body)

    return "OK"

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080")
    )	