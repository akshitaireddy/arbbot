from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='../deal-ui/build', static_url_path='/')