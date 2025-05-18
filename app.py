from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)
local_data = pd.read_csv('data/cleaned_movies.csv')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()

    # Ex: API (weather)
    if 'weather' in user_input:
        city = user_input.split()[-1]
        try:
            r = requests.get(f'https://api.weatherapi.com/v1/current.json?key=API_KEY&q={city}')
            weather = r.json()['current']['condition']['text']
            return jsonify({"response": f"The weather in {city} is {weather}."})
        except Exception as e:
            return jsonify({"error": str(e)})

    # Ex: Local (movie info)
    elif 'movie' in user_input:
        matches = local_data[local_data['title'].str.contains('back to the future', case=False)]
        if not matches.empty:
            return jsonify({"response": f"Found {len(matches)} results for that movie."})
        return jsonify({"response": "Movie not found in local data."})

    else:
        return jsonify({"response": "I'm not sure how to help with that."})
