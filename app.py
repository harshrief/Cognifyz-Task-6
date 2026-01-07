from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.select(".athing")[:10]:
        title = item.select_one(".titleline a").text
        link = item.select_one(".titleline a")["href"]
        articles.append({"title": title, "link": link})

    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
