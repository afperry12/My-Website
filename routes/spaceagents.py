from flask import Blueprint, render_template

bp = Blueprint('spaceagents', __name__)

@bp.route('/')
def home():
    return render_template('spaceagents.html')
