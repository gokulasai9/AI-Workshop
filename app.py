from flask import Flask 

app = Flask(__name__)

@app.route('/')
def homePage():
    return("Hello... I'm Gokul")

if (__name__ == "__main__"):
    app.run()
