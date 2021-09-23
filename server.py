from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route ('/play/<num>/<color>' ,methods=['GET'])
def boxes(num,color):
    numberofboxes = int(num)
    colorofboxes = str(color)
    return render_template('index.html',number = numberofboxes, color = colorofboxes)


if __name__ == "__main__":
    app.run( debug = True )