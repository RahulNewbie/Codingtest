
from lxml import html
import requests
import json
import io

#Global variables
pageURL = 'http://www.metacritic.com/game/playstation-4'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
jsonData = {}

#This method will make json object out of a dataset
def make_json(games,scores):
  #making dictionary from the two lists
  jsonData = dict(zip(games,scores))
  #making json structure out of title and score
  d = {'':[{'Title':k,'score':v} for k,v in jsonData.items()]}
  return json.dumps([{'Title': k, 'score': v} for k,v in jsonData.items()], indent=4, sort_keys = True)

#This method will open the url and return the content
def open_page():
  req = requests.get(pageURL,headers=hdr)
  return req

#This method will use lxml to transform the content as tree and travarse the tree to fetch the top games and their respective scores
def get_Top_Games():
  req=open_page()
  #using lxml.html library to make the url in content in tree like structure
  tree = html.fromstring(req.content)
  #Preparation of xpaths
  top_releases=tree.xpath('.//*[@class="clamp-list"]/tr//td[@class="clamp-summary-wrap"]/a[@class="title"]/h3/text()')
  games = [i.strip() for i in top_releases]
  scores=tree.xpath('.//*[@class="clamp-list"]/tr//div[@class="clamp-score-wrap"]/a/div[@class="metascore_w large game positive"]/text()')
  outPut=make_json(games,scores)
  print outPut

def main():
  get_Top_Games()


if __name__== "__main__":
  main()


