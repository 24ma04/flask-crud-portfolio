# Flask CRUD アプリ（ポートフォリオ）

## 概要
Python と Flask を用いて作成した Web ベースの CRUD アプリケーションです。  
データの登録・編集・削除を Web 上で行うことができ、  
誤操作防止のため削除時には確認ダイアログを表示します。

## 工夫した点
- 削除操作時に確認ダイアログを表示し、誤操作を防止
- 入力値チェックを行い、不正なデータ登録を防ぐ設計
- 画面遷移と処理の流れが分かりやすい構成を意識

## 機能
- カードの一覧表示
- 新規カードの追加
- 既存カードの編集
- カードの削除

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
- SQLite
- Bootstrap

## 実行方法（任意）
1. 仮想環境を有効化
```bat
.\venv\Scripts\activate
