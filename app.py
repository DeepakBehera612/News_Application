from flask import Flask, render_template
import requests
from datetime import datetime
import os
from dotenv import load_dotenv


app = Flask(__name__)


load_dotenv()
api_key = os.getenv('key')

@app.route('/')
def index():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    r = requests.get(url).json()
    cases = {
        'articles':r['articles']       
    }   

    return render_template("index.html",case=cases)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


if __name__ == "__main__":
    app.run(debug=True)
