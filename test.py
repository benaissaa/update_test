import pytest
from app_api.run import create_app
from app_api.Model.db import db as _db
from app_api.Model import Account, Mall, Unit
import json
import unittest

from flask import *

@pytest.fixture

def app(self):
    app = create_app()
    app.config.from_object(self)
    return app    

@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def db(app):
    _db.app = app
    _db.session.expire_on_commit = False

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def account(db):
    account = Account(name="test account")
    db.session.add(account)
    db.session.commit()
    return account


@pytest.fixture
def mall(db, account):
    mall = Mall(name="test mall", account_id=account.id)
    db.session.add(mall)
    db.session.commit()
    return mall


@pytest.fixture
def unit(db, mall):
    unit = Unit(name="test unit", mall_id=mall.id)
    db.session.add(unit)
    db.session.commit()
    return mall  

class TestGetAccounts:

    def test_get_accounts(self, client, db, account):
        response = client.get('/accounts')
        response_json = response.get_json()

        assert response.status_code == 200
        assert len(response_json["accounts"]) == 1


class TestGetAccount:

    def test_get_account_found(self, client, account):
        response = client.get(f'/accounts/{account.id}')
        response_json = response.get_json()    

class TestGetMalls:

    def test_get_malls(self, client, db, mall):
        response = client.get('/api/malls')
        response_json = response.get_json()

        assert response.status_code == 200
        assert len(response_json["malls"]) == 1            
