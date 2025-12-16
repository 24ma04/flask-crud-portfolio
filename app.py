from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# データベースモデル
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))

# 初期ページ（一覧表示）
@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

# プロジェクト追加
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        new_project = Project(title=title, description=description)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")

# プロジェクト編集
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    project = Project.query.get(id)
    if request.method == "POST":
        project.title = request.form['title']
        project.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", project=project)

# プロジェクト削除
@app.route("/delete/<int:id>")
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ここでテーブル作成
    app.run(debug=True)

