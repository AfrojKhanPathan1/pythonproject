from app import create_app, db

from app.auth.models import User
from sqlalchemy import exc

flask_app = create_app('prod')

# flask gives us to ability to run multiple application with each set of config
# tell to flask use current application context

with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='aaa').first():
            User.create_user(user='aaa', email='aaaa@thinkitive.com', password='11121997')
    except exc.IntegrityError:
        flask_app.run()

# https://flask-bookcatalog.herokuapp.com/
