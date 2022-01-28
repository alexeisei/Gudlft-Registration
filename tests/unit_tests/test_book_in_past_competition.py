from datetime import datetime
import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients
  
  
  def test_new_competitions_dates(client):
      date = datetime.today()
      date_competition = datetime.strptime(server.competitions[0]['date'], '%Y-%m-%d %H:%M:%S')
      print(date)
      print(date_competition)
      if date_competition > date :
         print(date)
         print(date_competition)
         assert date_competition == True
          
