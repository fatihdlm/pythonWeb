from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    names=["fatih","murat","bülent"]
    return render_template("site/index.html",names=names)

if __name__ == '__main__':
    app.run()
