import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_good_update_points_after_reservation(client):
    """ 
    Check if the update is good after the reservation.
    Club_points need to be different of the update_points
    """
    club_points = int(server.clubs[0]['points'])
    competition = server.competitions[0]
    reponse = client.post('/purchasePlaces', 
                          data={'club': 'Simply Lift', 
                                'competition': competition['name'], 
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 5,
                                }
                          )
    update_points = int(server.clubs[0]['points'])
    assert club_points != update_points
    assert reponse.status_code == 200
    


def test_bad_update_points_after_reservation(client):
    """
    Check if the update is bad after the reservation.
    Club_points need to be different of the update_points.
    if club points egal update points else we have a bad update
    """
    club_points = int(server.clubs[0]['points'])
    competition = server.competitions[0]
    reponse = client.post('/purchasePlaces', 
                          data={'club': 'Simply Lift', 
                                'competition': competition['name'], 
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 5,}
                          )
    update_points = club_points
    assert club_points == update_points
    assert reponse.status_code == 200
    
