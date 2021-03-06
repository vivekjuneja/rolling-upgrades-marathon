from flask import Flask, jsonify, request
import requests
import sys
import socket
import signal

app = Flask(__name__)
callee_addr = None
isHealthy = True

def handle_sigterm(signo, stack_frame):
    global isHealthy
    isHealthy = False
    print "I got Terminated"

def handle_sigkill(signo, stack_frame):
    print "I got Killed"

def handle_sighup(signo, stack_frame):
    print "I got hanged up"
   
signal.signal(signal.SIGTERM, handle_sigterm)
#signal.signal(signal.SIGKILL, handle_sigkill)
signal.signal(signal.SIGHUP, handle_sighup)

@app.route("/isHealthy")
def health():
    if isHealthy:
	return 'OK'
    return 'Shutting down', 503

@app.route('/caller', methods=['GET'])
def get_task1():
    _id = request.args.get('id')
    print requests.get('http://'+callee_addr+'/callee')
    return jsonify({'task': 'Work of Caller is over !', 'hostname' : socket.gethostname(), 'id': _id})


if __name__ == '__main__':
    port = sys.argv[1]
    callee_addr = sys.argv[2]
    print 'Starting the Caller at port ' + port + ', and will connect to ' + callee_addr
    app.run(port=int(port), debug=False,host='0.0.0.0')
