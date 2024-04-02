from flask import Flask, jsonify, render_template, request
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    # Call opensearch.py with subprocess. Adjust the path to opensearch.py as necessary.
    result = subprocess.run(['python3', 'opensearch.py', 'get', search_term], capture_output=True, text=True)
    if result.stderr:
        print("Error:", result.stderr)
        return jsonify(error="Search failed"), 500
    try:
        search_results = json.loads(result.stdout)
    except json.JSONDecodeError:
        return jsonify(error="Invalid response from search"), 500
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(port="8000")