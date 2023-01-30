from flask import Flask, render_template

app = Flask(__name__)

@app.route("/tic-tac-toe")
def board():
    return render_template("on_click.html")

@app.route('/background_process')
def background_process():
    print("Hello")
    return ("nothing")

if __name__ == "__main__":
    app.run(debug=True)
