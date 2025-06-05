from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/about')
def about():
    return jsonify({
        "name": "Trần Hoài An",
        "job": "Lập trình viên",
        "bio": "Tôi thích học Flask và phát triển phần mềm."
    })
import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
