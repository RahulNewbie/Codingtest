from lxml import html
from flask import Flask
import requests
import json
import io
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

#glaobal variable
pageURL = 'http://www.metacritic.com/game/playstation-4'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


@app.route("/")
def hello():
   app.logger.info('Info')
   return "Welcome to Meta Critic game page! For more info about games use <url>/games. For a specific one use <url>/games/Title-of-the-game"

#This method is to extract the data from url page and make an dictionary 
def get_data():
  jsonData = {}
  req = requests.get(pageURL,headers=hdr)
  #using lxml.html library to make the url in content in tree like structure
  tree = html.fromstring(req.content)
  app.logger.info('Accessing Webpage to get the content')
  try:
    #Preparation of xpaths
    top_releases=tree.xpath('.//*[@class="clamp-list"]/tr//td[@class="clamp-summary-wrap"]/a[@class="title"]/h3/text()')
    games = [i.strip() for i in top_releases]
    scores=tree.xpath('.//*[@class="clamp-list"]/tr//div[@class="clamp-score-wrap"]/a/div[@class="metascore_w large game positive"]/text()')
    #making dictionary from the two lists
    jsonData = dict(zip(games,scores))
  except:
    app.logger.error('An error occurred during acessing webpage')
  return jsonData


@app.route('/games/<string:title_of_game>')
def api_game_title(title_of_game):
  returnedJsonData=get_data()
  game_title= title_of_game
  #replacing underscore to space to get the actual title. Users are advised to use underscore in place of space because of curl msg.
  game_title = game_title.replace("_"," ")
  try:
    game_score= returnedJsonData[game_title]
  except:
    #if title doesnt match with the games in website
    app.logger.error('Error occured for the title of the game, Use \'_\' in spaces')
  output= json.dumps([{'Title': game_title, 'score': game_score}], indent=3)
  return output
  


@app.route('/games/')
def api_all_games():
  returnedJsonData=get_data()
  #making json structure out of title and score
  d = {'':[{'Title':key,'score':value} for key,value in returnedJsonData.items()]}
  output= json.dumps([{'Title': k, 'score': v} for k,v in returnedJsonData.items()], indent=3, sort_keys = True)
  return output


      
if __name__ == "__main__":
   #Logging 
   handler = RotatingFileHandler('log.txt', maxBytes=10000, backupCount=1)
   handler.setLevel(logging.INFO)
   app.logger.addHandler(handler)
   app.run()



