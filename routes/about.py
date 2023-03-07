# routes/about.py
from flask import Blueprint, render_template

bp = Blueprint('about', __name__)

@bp.route('/about')
def about():
    name = "Peter Perry"
    title = "Computer Scientist"
    bio = "I am a computer scientist with a passion for solving complex problems using code. I have experience in a variety of programming languages and frameworks, and I enjoy tackling new challenges and learning new technologies. In my free time, I enjoy working on personal projects and contributing to open source software."
    return render_template('about.html', name=name, title=title, bio=bio)
