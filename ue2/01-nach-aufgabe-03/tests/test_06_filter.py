def test_filter(client):
    assert [t['id'] for t in client.get('/todos?completed=false').json()]==[2,3]
    assert [t['id'] for t in client.get('/todos?completed=true').json()]==[1]
    assert client.get('/todos?completed=invalid').status_code==422

def test_formats(client):
    assert client.get('/demo/formats').json()['id']==1
    r=client.get('/demo/formats?format=xml')
    assert r.headers['content-type'].startswith('application/xml')
    assert '<id>1</id>' in r.text
    assert client.get('/demo/formats',headers={'Accept':'application/xml'}).text==r.text
