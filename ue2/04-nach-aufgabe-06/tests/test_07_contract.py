def test_contract(client):
    assert client.get('/health').json()=={'status':'ok'}
    paths=client.get('/openapi.json').json()['paths']
    assert set(paths['/todos'])=={'get','post'}
    assert set(paths['/todos/{id}'])=={'get','put','patch','delete'}
    assert client.get('/').status_code==200
    assert client.get('/docs').status_code==200
    assert client.post('/health').status_code==405
