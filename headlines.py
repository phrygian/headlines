import feedparser
from flask import Flask 

app = Flask(__name__)

RSS_FEEDS = {
	'bbc' : "http://feeds.bbci.co.uk/news/rss.xml",
	'cnn' : "http://rss.cnn.com/rss/edition.rss",
	'posttoday' : "https://www.posttoday.com/rss/src/breakingnews.xml",
	'sanook' : "http://rssfeeds.sanook.com/rss/feeds/sanook/news.index.xml"
}

@app.route('/')
def index():
	return "<h1>Rss Feed News</h1>"

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
	return """<html>
		<body>
			<h1>{3} Headlines News</h1>
			<b>{0}</b> <br />
			<i>{1}</i> <br />
			<p>{2}</p> <br />			
		</body>
	</html>""".format(first_article.get("title"), first_article.get("published"), \
		first_article.get("summary"), publication.upper())

if __name__ == '__main__':
	app.run(port=5000, debug=True)

