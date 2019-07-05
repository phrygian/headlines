import feedparser
from flask import Flask, render_template 

app = Flask(__name__)

RSS_FEEDS = {
	'bbc' : "http://feeds.bbci.co.uk/news/rss.xml",
	'cnn' : "http://rss.cnn.com/rss/edition.rss",
	'posttoday' : "https://www.posttoday.com/rss/src/breakingnews.xml",
	'sanook' : "http://rssfeeds.sanook.com/rss/feeds/sanook/news.index.xml"
}

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/bbc')
def bbc():
	return get_news('bbc')

@app.route('/cnn')
def cnn():
	return get_news('cnn')

@app.route('/sanook')
def sanook():
	return get_news('sanook')

@app.route('/posttoday')
def fox():
	return get_news('posttoday')

def get_news(publication):
	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	return render_template("home.html", article=first_article)

if __name__ == '__main__':
	app.run(port=5000, debug=True)

