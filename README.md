# week1-flask app

# Python Flaskフレームワークで入門ウェブアプリ作成、環境構築からデプロイまでを経験

- Python 3.11
- Flask 3.1.3
//Python用のフレームワーク、フレームワークとは、基本的な機能や構造をあらかじめ用意してある土台
flaskは軽量でWebアプリ作成に最適
- HTML / Jinja2
{{　variable }}のような形式でPythonのデータをHTMLに埋め込み可能、Jinja2使わないとばりだるい

## ローカルでの起動方法
```bash
git clone https://github.com/Midking-tpo/week1-flask.git
cd week1-flask
/opt/homebrew/bin/python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./venv/bin/python3 app.py
```

ブラウザで http://127.0.0.1:5000 を開く。


- Homebrew版Python 3.12ではvenvが作成できない問題に遭遇し、3.11で解決
- aliasの設定によりvenv内でも別のPythonが参照される問題をデバッグで特定