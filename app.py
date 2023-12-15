from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #this is for homepage!
def hello_world():
    return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)