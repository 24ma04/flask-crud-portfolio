# Flask CRUD アプリ（ポートフォリオ）

## 概要
Python と Flask を用いて作成した Web ベースの CRUD アプリケーションです。
データの登録・編集・削除を Web 上で行うことができ、誤操作防止のため削除時には確認ダイアログを表示します。
さらに、ログイン機能を追加し、ユーザーごとにデータを管理できるようになりました。

## 工夫した点
-　削除操作時に確認ダイアログを表示し、誤操作を防止
-　入力値チェックを行い、不正なデータ登録を防ぐ設計
-　画面遷移と処理の流れが分かりやすい構成を意識
-　ユーザー認証機能を追加し、未ログイン状態ではポートフォリオ画面にアクセスできないように制御

## 機能
- ログイン / ログアウト
- カードの一覧表示
- 新規カードの追加
- カードの編集
- カードの削除（削除確認ダイアログ付き）

## 初期ユーザー
- アプリ起動時に自動で作成される初期ユーザーです：

ユーザー名	   パスワード
test	       1234

※必要に応じて app.py 内でユーザーを追加してください。

## 今後の改善点
- 検索機能やページネーションの実装
- ユーザー登録機能の追加（現在は初期ユーザー固定）

## スクリーンショット
※ 下記画像は例です。実際のアプリ画面に置き換えてください

### トップページ（ログイン後）
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

## 動作確認
また、ブラウザ上で動作を確認できる [Replit版](https://replit.com/@aprilxxx666/flask-crud-portfolio) も用意しています。


## 実行方法（Windows）

```bash
git clone https://github.com/24ma04/flask-crud-portfolio.git
cd flask-crud-portfolio

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app.py
