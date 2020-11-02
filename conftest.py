import os
import pytest
from dotenv import load_dotenv

from links_transform import create_app
from links_transform import db

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    class settings_override:
        TESTING = True,
        SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    app = create_app(settings_override)
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


# @pytest.fixture(scope='session')
# def db(app, request):
#     def teardown():
#         _db.drop_all()
#
#     _db.app = app
#     _db.create_all()
#
#     request.addfinalizer(teardown)
#     return _db
#
#
# @pytest.fixture(scope='function')
# def session(db, request):
#     """Creates a new database session for a test."""
#     connection = db.engine.connect()
#     transaction = connection.begin()
#
#     options = dict(bind=connection, binds={})
#     session = db.create_scoped_session(options=options)
#
#     db.session = session
#
#     def teardown():
#         transaction.rollback()
#         connection.close()
#         session.remove()
#
#     request.addfinalizer(teardown)
#     return session

