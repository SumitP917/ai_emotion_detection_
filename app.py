from flask import Flask, render_template, request

app = Flask(__name__)

emotions = {
"happy":"😊",
"sad":"😢",
"angry":"😡",
"love":"😍",
"excited":"🤩",
"fear":"😨",
"surprise":"😲",
"bored":"😴",
"cool":"😎",
"confused":"😕",
"shy":"☺️",
"cry":"😭",
"laugh":"😂",
"thinking":"🤔",
"tired":"😫"
}

@app.route("/", methods=["GET","POST"])
def home():

    emotion=None
    emoji=None

    if request.method=="POST":

        text=request.form["text"].lower()

        for e in emotions:
            if e in text:
                emotion=e
                emoji=emotions[e]
                break

    return render_template("index.html",emotion=emotion,emoji=emoji)

app.run(debug=True)