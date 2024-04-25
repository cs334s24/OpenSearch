"""A simple Flask app that uses opensearch.py to search for dockets using a search term."""

import subprocess
import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Search for a term using opensearch.py."""
    search_term = request.form['search_term']

    command = ['python3', 'opensearch_connection.py', 'get', search_term]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
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
