import pytest

def test_create(client):
    r = client.post('/todos', json={'title':'Test'})
    assert r.status_code == 201
    assert r.json() == {'id':4,'title':'Test','completed':False}
    assert r.headers['location'] == '/todos/4'
    assert client.get('/todos/4').json() == r.json()

@pytest.mark.parametrize('body',[{}, {'title':''}, {'title':'   '}, {'title':123}, {'title':'x'*201}, {'title':'ok','completed':'true'}, {'title':'ok','id':9}])
def test_invalid(client,body):
    assert client.post('/todos',json=body).status_code == 422
