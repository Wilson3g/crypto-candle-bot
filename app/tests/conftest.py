import pytest
from app.app import create_app, db


@pytest.fixture(scope='module')
def client():
    app = create_app('testing')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 5

    ctx = app.app_context()
    ctx.push()
    yield app.test_client()
    ctx.pop()


@pytest.fixture(scope='module')
def banco():
    db.create_all()
    db.session.commit()
    yield db
    db.session.remove()
    db.drop_all()
