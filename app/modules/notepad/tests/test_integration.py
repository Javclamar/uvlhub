import pytest
from app import db
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.conftest import login, logout



@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email="user@example.com", password="test1234")
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user=user_test, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()
        
    yield test_client

def test_create_notepad_endpoint_returns_302(test_client):
    """
    POST /notepad/create (API JSON) debe crear un nuevo notepad y devolver status 200.
    """
    
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post('/notepad/create', json={'title': 'Nuevo notepad', 'body': 'Contenido del notepad'})
    assert response.status_code == 302, "Notepad creation did not return status 302."
