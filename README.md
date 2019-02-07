# Coding Challenge: HTML parsing

## Requirement   

Flask, lxml, request, logging, json,io
Please use pip to install dependencies 


## Installation

For parser.py(without flask app), use "python parser.py" and it will list down all the games as an array of JSON elements.

```bash
[
   {
      "Title": "Red Matter", 
      "score": "84"
   }, 
   {
      "Title": "Kingdom Hearts III", 
      "score": "85"
   }, 
...

```


For Flask app:

It can run in 2 ways:

Go to the respective directory and use python command to run the file ( python app.py) 

```bash
    rahul@rahul-HP-ProDesk-600-G1-TWR:~$ python app.py
    * Serving Flask app "app.py"
    * Environment: production
      WARNING: Do not use the development server in a production environment.
      Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

second way:

Use "export FLASK_APP=app.py" and type "python -m flask run" 

## Testing

curl msg to list down all games:

```bash
curl -X GET http://localhost:5000/games/
```

It will give a list of all top games present in the website along with their scores in json format. It can also be checked in a web browser by putting "http://127.0.0.1:5000/games/"


curl msg for specific game, when game title is given

```bash
curl -X GET http://localhost:5000/games/Tetris_Effect
```

This msg will give result in json format. This can be done in web browser too.

Please Note: While giving the game title in curl msg, please use '_' in place of space. As an example 

Tetris Effect -> Tetris_Effect


   
