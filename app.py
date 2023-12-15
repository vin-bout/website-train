from flask import Flask

app = Flask(__name__)

@app.route("/") #this is for homepage!
def hello_world():
    return "Hello, Vernika!"
print(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)