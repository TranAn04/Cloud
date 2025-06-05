from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/info', methods=['GET'])
def get_info():
    data = {
        "name": "Nguyễn Văn A",
        "email": "nguyenvana@example.com",
        "skills": ["Python", "Flask", "API", "Docker"]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
