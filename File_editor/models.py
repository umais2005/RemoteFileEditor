from datetime import datetime
from File_editor import db,login_manager,UserMixin

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    username = db.Column(db.String(20), unique=True,nullable=False)
    fullname = db.Column(db.String(50),nullable=False)
    userpassword = db.Column(db.String(30), nullable=False)
    files = db.relationship("File", backref="author", lazy=True)

    def __repr__(self) -> str:
        return f"User : {self.username},name: {self.fullname}"
  
class File(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(20), nullable=False,unique=False)
    date_modified = db.Column(db.DateTime ,nullable = False,default=datetime.utcnow)
    content = db.Column(db.String(256),default = "")
    filepassword = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") , nullable=False)

    def __repr__(self) -> str:
        return f"File {self.filename}"
    