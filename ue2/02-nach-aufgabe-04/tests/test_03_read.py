def test_read(client):
    assert client.get('/todos').status_code == 200
    assert len(client.get('/todos').json()) == 3
    assert client.get('/todos/1').json()['id'] == 1
    assert client.get('/todos/999').status_code == 404
    assert client.get('/todos/abc').status_code == 422
    assert client.get('/todos/0').status_code == 422
