import feedparser
import pyowm

from flask import Flask, render_template, request 

owm = pyowm.OWM('09eae7f84a2bf6a02bb93e9f31ee80a8')
observation = owm.weather_at_place('Bangkok, TH')
w = observation.get_weather()
print(type(w)) 

app = Flask(__name__)

RSS_FEEDS = {
	'bbc' : "http://feeds.bbci.co.uk/news/rss.xml",
	'cnn' : "http://rss.cnn.com/rss/edition.rss",
	'posttoday' : "https://www.posttoday.com/rss/src/breakingnews.xml",
	'sanook' : "http://rssfeeds.sanook.com/rss/feeds/sanook/news.index.xml"
}

@app.route('/', methods=['GET', 'POST'])
def get_news():
	query = request.args.get("publication")
	
	if not query or query.lower() not in RSS_FEEDS:
		publication = "bbc"
	else:
		publication = query.lower()

	feed = feedparser.parse(RSS_FEEDS[publication])	
	return render_template("home.html", 
				articles=feed['entries'],
				t=w.get_temperature('celsius'),
				h=w.get_humidity())

if __name__ == '__main__':
	app.run(port=5000, debug=True)