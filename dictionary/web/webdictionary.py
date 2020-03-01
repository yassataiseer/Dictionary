
from flask import Flask, render_template,request,session
import json
import urllib.request
import requests
import sqlite3 
  
conn = sqlite3.connect('dictionary.db', check_same_thread=False) 
c = conn.cursor() 
  
c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)') 


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("word.html")

@app.route('/', methods=['POST'])
def getvalue():
    try:
        word= request.form['text']
        url = f"""https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}"""
        rawData = requests.get(url).json()
        data = rawData[0]['meaning']['noun'][0]['definition']
        print( f"""The definition for that word is: {data}""")
        c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (word, data)) 
        conn.commit() 
        return render_template("count.html",word=word,data=data) 
    except:
        return "Invalid Input"

    exit()

    getvalue() 
    c.close() 
    conn.close() 

    




if __name__ == '__main__':
    app.run(debug=True)







