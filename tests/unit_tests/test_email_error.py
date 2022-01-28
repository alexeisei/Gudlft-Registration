import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_unknown_email():
    reponse = client.post('/showSummary',
                           data={'email': 'random@test.com'})
    assert reponse


def test_empty_email():
    reponse = client.post('/showSummary',
                           data={'email': ''})
    assert reponse


def test_known_email():
    reponse = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'})
    assert reponse

def test_not_a_email():
    reponse = client.post('/showSummary',
                           data={'email': '12345abcd'})
    assert reponse
    
