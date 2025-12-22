# Flask CRUD アプリ（ポートフォリオ）

## 概要
Python と Flask を用いて作成した Web ベースの CRUD アプリケーションです。  
データの登録・編集・削除を Web 上で行うことができ、  
誤操作防止のため削除時には確認ダイアログを表示します。

## 工夫した点
- 削除操作時に確認ダイアログを表示し、誤操作を防止しました
- 入力値チェックを行い、不正なデータ登録を防ぐ設計にしました
- 画面遷移と処理の流れが分かりやすい構成を意識しました

## 機能
- カードの一覧表示
- 新規カードの追加
- カードの編集
- カードの削除（削除確認ダイアログ付き）

## 今後の改善点
- ログイン機能の追加
- 検索機能やページネーションの実装

## スクリーンショット
※ 下記画像は例です。実際のアプリ画面に置き換えてください

### トップページ
![トップページ](static/screenshots/screenshot_top.png)

### 新規追加ページ
![追加ページ](static/screenshots/screenshot_add.png)

### 編集ページ
![編集ページ](static/screenshots/screenshot_edit.png)

### 削除確認ダイアログ
![削除確認ダイアログ](static/screenshots/screenshot_delete_confirm.png)


## 技術スタック
- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- HTML / CSS
- JavaScript


## 実行方法（Windows）

```bash
git clone https://github.com/24ma04/flask-crud-portfolio.git
cd flask-crud-portfolio

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app.py
