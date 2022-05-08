from unicodedata import category
from flask import Blueprint,render_template,request,flash,jsonify
# from flask_login import  login_required,current_user
# from .models import Note
# from .main import db
# import json


views = Blueprint('views',__name__)

@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    # if request.method=='POST':
    #     note=request.form.get('note')

    #     if len(note)<1:
    #         flash('note is too short', category='error')
    #     else:
    #         new_note=Note(data=note,user_id=current_user)
    #         db.session.add(new_note)
    #         db.session.commit()

    #         flash('note created successfuly', category='success')

    return render_template("home.html")

# @views.route('/delete-note',method=['POST'])
# def delete_note():
#     note=json.loads(request.data)
#     noteId=note['noteId']
#     note=Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})



