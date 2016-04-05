from flask import Flask, jsonify
import requests
import time
import sys

app = Flask(__name__)
port = None
sleep_seconds = None

@app.route('/callee', methods=['GET'])
def get_task2(): 
    time.sleep(int(sleep_seconds))
    return jsonify({'task': 'Callee received the message. Says Thanks!'})

if __name__ == '__main__':
    port = sys.argv[1]
    sleep_seconds = sys.argv[2]
    print 'Connecting to ' + port + ' and will sleep for ' + sleep_seconds
    app.run(port=int(port),debug=False,host='0.0.0.0')
