#!/usr/bin/env python
from flask import Flask, url_for, request, json
import random

app = Flask(__name__)

@app.route('/bot', methods = ['POST'])
def api_bot():
    try:
        game = request.json
        betting = game['betting']
        print betting
        random.seed()
        if betting['canRaise']:
            choice = random.randrange(1,4,1) 
            if choice == 1:
                print "fold"
                return "0"
            elif choice == 2:
                print "check"
                return str( betting['call'] )
            else:
                print "raise"
                return str( betting['raise'] * random.randrange(1,5,1) ) 
        else:
            choice = random.randrange(1,3,1) 
            if choice ==  1:
                print "fold"
                return "0"
            else:
                print "check"
                return str( betting['call'])
    except RuntimeException as e: 
        print e
        raise e


if __name__ == '__main__':
    app.run()
