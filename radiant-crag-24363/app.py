from flask import Flask, render_template, request, redirect, url_for
#import datetime as dt
#import pandas as pd 
#import pandas_datareader.data as web

app = Flask(__name__)

#@app.route('/')
#def index():
#  return render_template('index.html')

@app.route('/')
def start():
    #return "hello!"
    return render_template('form.html')

@app.route('/example')#, methods=['GET'])
def example():
    return "Thank you!  I have a graph that worked locally but not on Heroku; please see gitHub page for details."
    #return "hello"
    #ticker = "hello"
    #ticker = (request.form['ticker'])#new
    #ticker = 'TSLA'
    #start = dt.datetime(2019,1,1)
    #end = dt.datetime(2019,1,31)
    #PULL DATA FROM WEB
    #df = web.DataReader(ticker, 'yahoo', start, end) #TSLA = tesla
    #return str(len(df))

#@app.route('/about')
#def about():
#  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
