import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_user(client):
    response = client.get('/')

    club = server.clubs[2]
    competition = server.competitions[0]

    assert response.status_code == 200
    response = client.post('/showSummary',
                          data={'email': club['email']})
    assert b'Welcome, kate@shelifts.co.uk' in response.data
    assert response.status_code == 200

    points = int(club['points'])
    response = client.post('/purchasePlaces',
                          data={'club': club['name'],
                                'competition': competition['name'],
                                'places': 1}
                          )
    updated_points = int(club['points'])
    assert response.status_code == 200
    assert updated_points != points

    points = int(club['points'])
    response = client.post('/purchasePlaces',
                          data={'club': club['name'],
                                'competition': competition['name'],
                                'places': 13}
                          )
    updated_points = int(club['points'])
    assert response.status_code == 200
    assert updated_points == points
