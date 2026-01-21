import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# --- Flask 設定 ---
app = Flask(__name__)
app.secret_key = "secret"

# --- DB 設定 ---
base_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(base_dir, "database.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_file}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Flask-Login 設定 ---
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# --- モデル ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- ルート ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash("ログイン失敗")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", projects=projects)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
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

        new_project = Project(title=title, description=description, user_id=current_user.id)
        db.session.add(new_project)
        db.session.commit()
        flash("追加しました")
        return redirect(url_for('index'))

    return render_template("add.html")

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    project = Project.query.get_or_404(id)
    if project.user_id != current_user.id:
        flash("権限がありません")
        return redirect(url_for('index'))

    if request.method == 'POST':
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

@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    project = Project.query.get_or_404(id)
    if project.user_id != current_user.id:
        flash("権限がありません")
        return redirect(url_for('index'))

    db.session.delete(project)
    db.session.commit()
    flash("削除しました")
    return redirect(url_for('index'))

# --- DB 初期化 & 起動 ---
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # DB 作成
        print(f"database.db を作成しました: {db_file}")

        # 初回ユーザー作成
        if not User.query.filter_by(username="test").first():
            user = User(username="test")
            user.set_password("1234")
            db.session.add(user)
            db.session.commit()
            print("初回ユーザーを作成しました: test / 1234")

    # Flask 起動
    app.run(debug=True)
