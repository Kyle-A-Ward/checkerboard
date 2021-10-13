from flask import Flask, render_template
app = Flask(__name__)

@app.route('/test')
def original():
    return render_template("index.html", x=8, y=8)

@app.route('/<y>')
def row(y):
    y = int(y)
    return render_template("index.html", x=8, y=y)

@app.route('/<x>/<y>')
def rowcolumn(x, y):
    x = int(x)
    y = int(y)
    return render_template("index.html", x=x, y=y)

if __name__=="__main__":
    app.run(debug=True)