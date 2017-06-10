import os
from flask import Flask 
app = Flask(__name__)
# imports the appropriate app_settings variable depending on the environment
#app.config.from_object('module_name.ProductionConfig')

app.config.from_object(__name__) # load config from this file

app.config.update(dict(
  DEBUG = False,
  TESTING = False,
  SECRET_KEY = 'this-really-needs-to-be-changed'
  ))

@app.route('/')
def hello():
  return "Hello World!"

@app.route('/<name>')
def hello_name(name):
  return "Hello {}!".format(name)

if __name__ == '__main__':
  app.run()