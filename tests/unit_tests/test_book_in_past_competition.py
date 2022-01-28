from datetime import datetime
import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_new_competitions_dates(client):
    """
    check if the competition date is still valid
    """
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    
    result = client.post('/purchasePlaces', 
                         data={'club': club,
                                'competition': competition['name'],
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 5,
                               })
    assert result.status_code == 200

     
def test_past_competitions_dates(client):
    """
    check if the date of the competition is no longer valid
    """
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces', 
                         data={'club': club,
                                'competition': competition['name'],
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 5,
                               })
    assert result.status_code == 200
    
    
def test_booking_competition_good(client):
    
    club= server.clubs[0]['name']
    competition = server.competitions[0]['name']
    result = client.get(f'/book/{competition}/{club}')
    
    assert result.status_code == 200
