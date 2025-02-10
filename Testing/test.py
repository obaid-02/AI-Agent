import pytest
import sys
import os

# Add the parent directory to the system path so that app.py can be found
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    # print(response.data)
    assert response.status_code == 200
    assert b"Mudkudu" in response.data
    # print(response.data)

def test_news_page(client):
    response = client.post('/news', data={'company': 'Google'})
    assert response.status_code == 200
    assert b"Latest News" in response.data
    # print(response.data)

if __name__ == '__main__':

    result = pytest.main(["-v", "--disable-warnings"])
    if result == 0:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
