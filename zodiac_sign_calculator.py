#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:10:06 2023

@author: stevens
"""
from flask import Flask, request, jsonify
import datetime

app = Flask(__name)

# Function to calculate the zodiac sign based on the date of birth
def calculate_zodiac_sign(dob):
    if (dob.month == 3 and dob.day >= 21) or (dob.month == 4 and dob.day <= 19):
        return "Aries"
    elif (dob.month == 4 and dob.day >= 20) or (dob.month == 5 and dob.day <= 20):
        return "Taurus"
    elif (dob.month == 5 and dob.day >= 21) or (dob.month == 6 and dob.day <= 20):
        return "Gemini"
    elif (dob.month == 6 and dob.day >= 21) or (dob.month == 7 and dob.day <= 22):
        return "Cancer"
    elif (dob.month == 7 and dob.day >= 23) or (dob.month == 8 and dob.day <= 22):
        return "Leo"
    elif (dob.month == 8 and dob.day >= 23) or (dob.month == 9 and dob.day <= 22):
        return "Virgo"
    elif (dob.month == 9 and dob.day >= 23) or (dob.month == 10 and dob.day <= 22):
        return "Libra"
    elif (dob.month == 10 and dob.day >= 23) or (dob.month == 11 and dob.day <= 21):
        return "Scorpio"
    elif (dob.month == 11 and dob.day >= 22) or (dob.month == 12 and dob.day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

@app.route('/calculate_zodiac', methods=['GET'])
def calculate_zodiac():
    dob = request.args.get('dob')
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    zodiac = calculate_zodiac_sign(dob)
    return jsonify({'zodiac': zodiac})

if __name__ == '__main__':
    app.run(debug=True)

