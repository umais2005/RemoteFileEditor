from File_editor.models import User,File
from File_editor import db , app

app.app_context().push()
db.create_all()
db.session.commit()