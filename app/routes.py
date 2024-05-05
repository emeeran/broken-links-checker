from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from .utils import extract_links, is_valid
from .modules import db

app = Flask(__name__)


@app.route("/check", methods=["POST"])
def check_url():
    # Your route implementation here
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "Missing URL parameter"}), 400

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"error": "Invalid URL"}), 400

        soup = BeautifulSoup(response.text, "html.parser")
        links = extract_links(soup)
        valid_links = [link for link in links if is_valid(link)]

        return jsonify({"valid_links": valid_links}), 200

    except requests.exceptions.RequestException as e:
        return jsonify(
            {"error": "An error occurred while checking the URL"}), 500
