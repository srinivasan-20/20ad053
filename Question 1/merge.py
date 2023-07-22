from flask import Flask, request, jsonify

app_server = Flask(__name__)

@app_server.route('/display_merged_list', methods=['POST'])
def display_merged_list():
    data = request.get_json()
    merged_list = data.get('merged_list', [])
    return jsonify(numbers=merged_list)

if __name__ == '__main__':
    app_server.run(port=8001)

