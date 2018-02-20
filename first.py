

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    names =["fatih","dilmaç","deneme"]
    return render_template("index.html",names=names)

if __name__ == "__main__":
    app.run()
