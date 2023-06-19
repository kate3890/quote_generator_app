from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the response to JSON
        return data['content'], data['author']  # Return the quote and the author
    return "Error: Unable to retrieve quote", ""  # Return an error message if the request was unsuccessful

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/quote')
def quote():
    quote, author = get_quote()
    return render_template("quote.html", quote=quote, author=author)

if __name__ == "__main__":
    app.run(debug=True)
