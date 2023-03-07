from flask import Blueprint, render_template

bp = Blueprint('brainmap', __name__)

@bp.route('/brainmap')
def brainmap():
    return render_template('brainmap.html')
