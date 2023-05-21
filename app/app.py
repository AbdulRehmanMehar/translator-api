from flask import Flask, jsonify, request
from .utils.translator import list_languages, translate
from threading import Thread
import multiprocessing


app = Flask(__name__)

@app.route("/list-languages")
def list_langs():
    return jsonify(list_languages())
    

@app.route("/translate", methods=['POST'])
def translate_it():
    body = request.get_json()
    langs = list_languages()
    
    text = body.get('text')
    source = body.get('source')
    target = body.get('target')

    if (text is None or
        source is None or
        target is None or
        langs.get(source) is None or
        langs.get(target) is None):

        return "invalid data"

    return translate(text, source, target)