from flask import Flask, render_template, request
import requests

# Create Flask instance
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
# Simple home page, title, and button to trigger API request and page redirect
def index():
    return render_template('home.html')


@app.route('/options', methods=['GET', 'POST'])
# Generate two random wikipeda article topics using Wikipedia Random API
def get_article_options():
    # Make API Request
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "2",
        "rnnamespace": "0",
    }
    res = S.get(url=URL, params=parameters)
    data = res.json()

    # Create a dict for the two options. This dict will be passed to the HTML template
    # The title will be used for the button label.
    # The id will be used to generate a link to the wiki page.
    article_options = {
        'one': {
            'title': data['query']['random'][0]['title'],
            'id': data['query']['random'][0]['id']
        },
        'two': {
            'title': data['query']['random'][1]['title'],
            'id': data['query']['random'][1]['id']
        }
    }
    return render_template('options.html', article_options=article_options)


if __name__ == "__main__":
    app.run(debug=True)
