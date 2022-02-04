import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_unknow_email():
    reponse = client.post('/showSummary',
                           data={'email': 'random@test.com'})
    assert reponse.status_code == 302


def test_empty_email():
    reponse = client.post('/showSummary',
                           data={'email': ''})
    assert reponse.status_code == 302


def test_know_email():
    reponse = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'})
    assert reponse.status_code == 200

def test_not_a_email():
    reponse = client.post('/showSummary',
                           data={'email': '12345abcde'})
    assert reponse.status_code == 302


def test_logout():
	reponse = client.get('/logout')
	assert reponse.status_code == 302
 
def test_index():
	reponse = client.get('/')
	assert reponse.status_code == 200
