from flask import Flask, jsonify
pip install requests
import requests

app_client = Flask(__name__)

def fetch_data_from_links(links):
    merged_list = []
    for link in links:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    merged_list.extend(data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {link}: {e}")
    return merged_list

@app_client.route('/get_merged_list', methods=['GET'])
def get_merged_list():
    links = [
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd"
    ]
    merged_list = fetch_data_from_links(links)
    return jsonify(merged_list=merged_list)

if __name__ == '__main__':
    app_client.run(port=8000)
