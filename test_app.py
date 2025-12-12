import pytest
import os
os.environ["TEST_DB"] = "test_tasks.db"
from app import app
import database as db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists("test_tasks.db"):
        os.remove("test_tasks.db")
    db.create_table()
    with app.test_client() as client:
        yield client
    if os.path.exists("test_tasks.db"):
        os.remove("test_tasks.db")

def test_add_note(client):
    response = client.post('/api/notes/' , json= {'title' : 'first note' , 'content' : 'first content to know about'})
    assert response.status_code == 201
    assert 'message' in response.json
def test_get_all_notes(client):
    client.post('/api/notes/' , json= {'title' : 'fake One' , 'content' : 'FAKE content to know about'})
    response = client.get('/api/notes/')
    assert isinstance(response.json , list) == True
    assert response.status_code == 200    

def test_get_single_note(client):
    client.post('/api/notes/' , json= {'title' : 'fake One' , 'content' : 'FAKE content to know about'})
    response = client.get('/api/notes/1')
    print(f"Response JSON: {response.json}")  # ← Add this
    print(f"Response status: {response.status_code}")  # ← Add this
    
    
    assert response.json['id'] == 1
    assert response.status_code == 200 
    
def test_update_note(client):
    client.post('/api/notes/' , json= {'title' : 'fake One' , 'content' : 'FAKE content to know about'})
    
    response = client.put('/api/notes/1' , json= {'title' : 'New UPdate' , 'content' : 'FAKE New Update'}) 
    assert response.status_code == 200 
    assert 'message' in response.json
def test_delete_note(client):
    client.post('/api/notes/' , json= {'title' : 'fake One' , 'content' : 'FAKE content to know about'})
    response = client.delete('/api/notes/1')
    assert response.status_code == 200 
    assert 'message' in response.json              
