from flask import Flask, render_template

import urllib.request
import json
#import webbrowser

app = Flask(__name__)

@app.route("/")
def hello():
	##URL with API Key
	apodurl = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

	##Calling the web service
	apodurlobj = urllib.request.urlopen(apodurl)

	apodread = apodurlobj.read()
	## Decode JSON to Python Data Structure(Dictionary)
	## Basically converts JSON format to Dictionary format as Python can only understand Dictionary
	decodeapod = json.loads(apodread.decode('utf-8'))

	image = decodeapod ['url']


	##input('\nPress Enter to open NASA Picture of the Day in Firefox')
	##webbrowser.open(decodeapod['url'])
	return render_template('index.html', picture = image)

if __name__ == '__main__':
   app.run(debug = True)