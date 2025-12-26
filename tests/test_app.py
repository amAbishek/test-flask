from app import app

def test_home_page_status():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_home_page_content():
    client = app.test_client()
    response = client.get("/")
    assert b"<html" in response.data
