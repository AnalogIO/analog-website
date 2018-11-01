# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:53:24 2018

@author: base
"""


from flask import Flask, render_template, request, redirect, jsonify, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontPage():
    
    return render_template('index.html')




if __name__ == '__main__':
    try:
        app.run(port=8000, debug=True, use_reloader=False)
    except KeyBoardInterrupt:
        app.close()
        
