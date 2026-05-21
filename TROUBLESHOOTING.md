# 環境構築トラブルシューティング記録

## 発生した問題と解決策

### 問題1: python3コマンドが古いバージョン(3.9.6)を参照していた

**症状**
```bash
python3 --version  # Python 3.9.6 と表示される
```

**原因**  
MacにはデフォルトでPython 3.9.6が `/usr/bin/python3` に入っている。
ターミナルはPATHの順番に従ってコマンドを探すため、Homebrewで新しく入れた
Pythonより先にシステムのPythonが見つかってしまっていた。

**解決策**  
`.zshrc` にaliasを追加して、python3と打ったら必ず3.11を使うよう設定した。
```bash
echo 'alias python3="/opt/homebrew/bin/python3.11"' >> ~/.zshrc
source ~/.zshrc
```

---

### 問題2: Homebrew版Python 3.12でvenv(仮想環境)が作れなかった

**症状**

Error: Command 'ensurepip' returned non-zero exit status 1.

**原因**  
Homebrew版Python 3.12以降は意図的に `ensurepip` を制限している仕様変更があった。
そのため `python -m venv` で仮想環境が作れなかった。

**参考**  
https://pakapaka.jp/homebrew-python-pip/

**解決策**  
Python 3.11を使うことで解決。
```bash
brew install python@3.11
/opt/homebrew/bin/python3.11 -m venv venv
```

---

### 問題3: venv有効化後もFlaskが見つからなかった

**症状**

ModuleNotFoundError: No module named 'flask'

**原因**  
`(venv)` は表示されていたが、`which python3` で確認すると
aliasのせいでvenv外のPythonが使われていた。

**解決策**  
venv内のPythonを直接指定して実行する。
```bash
./venv/bin/python3 app.py
```

---

## 学んだこと

- **PATHとは**: ターミナルがコマンドを探すフォルダの順番リスト。先に見つかった方が使われる
- **aliasとは**: コマンド名に別の命令を割り当てる設定。PATHより優先される
- **venvとは**: プロジェクトごとに独立したPython環境を作る仕組み。`(venv)` が表示されていても使われるPythonが正しいか `which python3` で確認が必要
- **Homebrew 3.12の罠**: 3.12以降はvenv作成に制限あり。3.11を使うのが現時点では安全

---

## venv（仮想環境）とは

### 一言で言うと
**プロジェクトごとに独立したPythonの部屋を作る仕組み**

**参考サイト**
https://qiita.com/probabilityhill/items/18b6ac07df89b9859fa4

https://zenn.dev/techcareer/articles/python-venv-complete-guide

### なぜ必要か？

venvなしだと、インストールしたライブラリが**Mac全体に影響する**。

例えば：
- アプリAはFlask 2.0が必要
- アプリBはFlask 3.0が必要

venvなしだと両立できない。どちらかしか入れられない。

venvありだと：

Mac本体のPython（触らない）
├── アプリA/
│   └── venv/  ← Flask 2.0が入ってる部屋
└── アプリB/
└── venv/  ← Flask 3.0が入ってる部屋

それぞれの部屋に好きなバージョンを入れられる。

### 基本的な使い方

```bash
# 仮想環境を作る（初回だけ）
python3 -m venv venv

# 仮想環境に入る（プロジェクト作業前に毎回やる）
source venv/bin/activate
# → (venv) が先頭に表示されたら入れてる状態

# 仮想環境から出る（作業終わったら）
deactivate
```

### GitHubにはvenvを上げない

venvフォルダは巨大（数十MB）で、他の人のPCの環境に依存するため上げない。
代わりに `requirements.txt` を上げることで、他の人が同じ環境を再現できる。

```bash
# 自分の環境のライブラリ一覧を記録
pip freeze > requirements.txt

# 他の人が再現するとき
pip install -r requirements.txt
```

### まとめ

| | venvなし | venvあり |
|---|---|---|
| ライブラリの影響範囲 | Mac全体 | そのプロジェクトだけ |
| バージョン管理 | 難しい | プロジェクトごとに自由 |
| チーム開発 | 環境がバラバラになりがち | requirements.txtで統一できる |