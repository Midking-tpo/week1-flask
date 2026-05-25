from flask import Flask, render_template
//ここでFlaskと、render?_templateインポート

app = Flask(__name__)
//Flaskクラスのインスタンスを作成、appという変数に代入

@app.route("/")
def index():
    return render_template("index.html", message="Hello,World!")

if __name__ == "__main__":
    app.run(debug=True)