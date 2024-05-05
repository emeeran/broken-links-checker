from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from .utils import extract_links, is_valid
from .models import db

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_url():
    # Your route implementation here
    pass
