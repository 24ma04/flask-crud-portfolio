import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret"  # flash用

db_file = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_file}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))

# --- ルート（元の index.html を維持） ---
@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')

        if not title or not description:
            flash("タイトルと説明は必須です")
            return redirect(url_for('add'))
        if len(title) > 100:
            flash("タイトルは100文字以内で入力してください")
            return redirect(url_for('add'))
        if len(description) > 200:
            flash("説明は200文字以内で入力してください")
            return redirect(url_for('add'))

        new_project = Project(title=title, description=description)
        db.session.add(new_project)
        db.session.commit()
        flash("追加しました")
        return redirect(url_for('index'))

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    project = Project.query.get_or_404(id)

    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')

        if not title or not description:
            flash("タイトルと説明は必須です")
            return redirect(url_for('edit', id=id))
        if len(title) > 100:
            flash("タイトルは100文字以内で入力してください")
            return redirect(url_for('edit', id=id))
        if len(description) > 200:
            flash("説明は200文字以内で入力してください")
            return redirect(url_for('edit', id=id))

        project.title = title
        project.description = description
        db.session.commit()
        flash("更新しました")
        return redirect(url_for('index'))

    return render_template("edit.html", project=project)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash("削除しました")
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        if not os.path.exists(db_file):
            db.create_all()
            print("database.db を作成しました。")
        else:
            print("database.db は既に存在します。")
    app.run(host='0.0.0.0', port=5000, debug=True)
