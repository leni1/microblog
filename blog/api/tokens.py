from flask import jsonify, g
from blog import db
from blog.api import bp
from blog.api.auth import basic_auth


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token': token})


def revoke_token():
    pass
