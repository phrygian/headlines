import feedparser
import pyowm
import time

from flask import Flask, render_template, request 

app = Flask(__name__)

owm = pyowm.OWM('09eae7f84a2bf6a02bb93e9f31ee80a8')
get_weather = owm.weather_at_place('Bangkok, TH')
weather = get_weather.get_weather()
read_time = time.gmtime(weather.get_reference_time())
location = get_weather.get_location()

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
				time=time.strftime("%x %X", read_time),
				location=location,
				icon=weather.get_weather_icon_url(),
				t=weather.get_temperature('celsius'),
				h=weather.get_humidity())

print(type(location))
print(dir(location))

if __name__ == '__main__':
	app.run(port=5000, debug=True)