

import json
import pytest
from flask import Flask
from app import db
from app.models import Employee, Company
from app.routes.database_routes import bp as database_bp



@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(database_bp)
    yield app
    with app.app_context():
        db.drop_all()


def test_insert_data_endpoint(app):
    client = app.test_client()

    response = client.post('/insert-data')

    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'Data inserted successfully'}

   
    with app.app_context():
        employee_count = db.session.query(Employee).count()
        company_count = db.session.query(Company).count()

    assert employee_count > 0
    assert company_count > 0


def test_insert_data_endpoint_error(app):
    client = app.test_client()

   
    with pytest.raises(Exception):
        response = client.post('/insert-data', data={'simulate_error': True})
        assert response.status_code == 500
        assert json.loads(response.data) == {'error': 'Simulated error message'}
