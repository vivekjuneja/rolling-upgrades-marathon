from flask import Flask, jsonify,request
import requests
import time
import sys
import socket
import signal

app = Flask(__name__)
app.debug=True
port = None
sleep_seconds = None

isHealthy = True

def handle_sigterm(signo, stack_frame):
    global isHealthy
    isHealthy = False
    print "I got Terminated"
    system.exit()

def handle_sighup(signo, stack_frame):
	global isHealthy
	isHealthy = False
	print "I got hanged up"



@app.route("/isHealthy")
def health():
    if isHealthy:
        return 'OK'
    return 'Shutting down', 503


@app.route('/callee', methods=['GET'])
def get_task2(): 
    _id = request.args.get('id')
    time.sleep(int(sleep_seconds))
    print _id
    return jsonify({'task': 'Callee received the message. Says Thanks!', 'callee_host':socket.gethostname(), 'processing_id': _id})

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, handle_sigterm)
    signal.signal(signal.SIGHUP, handle_sighup)
    port = sys.argv[1]
    sleep_seconds = sys.argv[2]
    print 'Connecting to ' + port + ' and will sleep for ' + sleep_seconds
    app.run(port=int(port),debug=False,host='0.0.0.0')
