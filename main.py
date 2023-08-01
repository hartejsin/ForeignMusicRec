## a flask app to take 5 songs from the user and return a new recommendation to them 
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import openai
import os 

load_dotenv()

##flask_app = os.environ.get('FLASK_APP')
app = Flask(__name__, template_folder= 'template', static_folder= 'static')
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/results', methods = ['POST'])
def reccomendation():
    
    if request.method == 'POST':
        name = request.form['name']
        song1 = request.form['song1']
        song2 = request.form['song2']
        song3 = request.form['song3']
        song4 = request.form['song4']
        song5 = request.form['song5']

    songs = f"{song1},{song2},{song3},{song4},{song5}"
    print(songs)
    instructions = "You will be provided a list of 5 songs. \
        Select a random language and generate a song reccomendation based on the list of songs"
    messages = [
        {"role": "system", "content": instructions},
    ]
    messages.append({"role": "user", "content": songs})
    rec = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 1,
        max_tokens = 2000,
    )
    
    recommendation_text = rec.choices[0].message['content']
    return render_template('result.html', recommendation=recommendation_text)



@app.route('/music')
def insert_songs():
    return render_template('music.html')


@app.route('/')
def landing_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)