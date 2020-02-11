from flask import Flask
from makeFolder import makeFolder
from makeFolder import getLatest

app = Flask(__name__)

@app.route("/")
def home():
    folder = getLatest()
    try:
        makeFolder()
        return "The following project was created: <br/> <br/> {}".format(folder)
    except:
        return 'The following project already exsists: <br/> <br/> {}'.format(folder)
    
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")