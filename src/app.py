from flask import Flask, jsonify
import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        "message": "Hello Json",
        'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
        'hostname' : socket.gethostname(),
        'message' : "You are doing great!",
        'message': "Welcome DevOps Engineer123"
    })

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'up'}), 200
if __name__ == '__main__':
    app.run(host="0.0.0.0")