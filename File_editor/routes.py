from flask import flash, render_template, url_for, redirect,request
from flask_login import current_user, login_required, login_user, logout_user
from File_editor.forms import LoginForm, CreateUser,CreateFile, TextArea
from File_editor.models import File,User
from File_editor import app, db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
login_manager.login_view = 'login'

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    files = File.query.all()
    return render_template("home.html",files=files,title="Homepage")

@app.route("/login",methods = ["POST","GET"])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.userpassword , form.password.data):
                login_user(user)
                flash('Login Success!')
                return redirect("home")
            else:
                flash("worng password or username")
                form.password.data = ''
                form.username.data = ''
    return render_template("login.html",form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("logged out!")
    redirect("home")
    return redirect("home")

current_user
@app.route("/create",methods=["POST","GET"])
@login_required
def create():
    form= CreateFile()
    if form.validate_on_submit():
        file_to_be_added = File(filename=form.filename.data,
                        filepassword=form.password.data,author=current_user)
        db.session.add(file_to_be_added)
        db.session.commit()
        return redirect("home")
    return render_template("create.html",form=form)


@app.route("/register",methods=["GET","POST"])
def register():
    form = CreateUser()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    fullname=form.fullname.data,userpassword=generate_password_hash(form.Password.data))
        db.session.add(user)
        db.session.commit()
        id = user.id
        form.username.data = ""
        form.fullname.data = ""
        flash(f"user added!")
        return redirect(url_for('login'))
    return render_template("register.html",form=form)

@app.route("/edit/<int:file_id>",methods=["POST", "GET"])
def update(file_id):
    file = File.query.get(file_id)
    form = TextArea()
    return render_template('update.html',file=file,form=form)
