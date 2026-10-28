import pytest
from app import create_app
from app.extensions import db
from app.config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False # Disable CSRF for testing simplicity

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_homepage_status(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Ahmad Alfan Ghofar' in response.data

def test_project_detail_status(client):
    # Seed a project first
    from app.models import Project
    with client.application.app_context():
        p = Project(title="Test", slug="test", short_description="Desc", full_description="Full", category="Cat", technologies="Tech")
        db.session.add(p)
        db.session.commit()
    
    response = client.get('/projects/test')
    assert response.status_code == 200

def test_404_page(client):
    response = client.get('/this-page-does-not-exist')
    assert response.status_code == 404
    assert b'404' in response.data

def test_contact_form_validation(client):
    # Test empty form
    response = client.post('/contact/send', data={})
    assert response.status_code == 302 # Redirects back due to validation failure
    
    # Test valid form (CSRF disabled in test config)
    response = client.post('/contact/send', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'subject': 'Test Subject',
        'message': 'This is a test message.'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'berhasil dikirim' in response.data

def test_cv_download_missing(client):
    response = client.get('/download-cv', follow_redirects=True)
    assert response.status_code == 200
    assert b'sedang disiapkan' in response.data