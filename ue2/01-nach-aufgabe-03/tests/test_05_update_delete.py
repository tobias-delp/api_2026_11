def test_update(client):
    assert client.put('/todos/1',json={'title':'Neu'}).status_code == 422
    r=client.put('/todos/1',json={'title':'Neu','completed':False})
    assert r.json()=={'id':1,'title':'Neu','completed':False}
    assert client.patch('/todos/1',json={'completed':True}).json()=={'id':1,'title':'Neu','completed':True}
    assert client.patch('/todos/1',json={'title':None}).status_code==422
    assert client.patch('/todos/999',json={'completed':True}).status_code==404
    assert client.put('/todos/999',json={'title':'x','completed':False}).status_code==404

def test_delete(client):
    r=client.delete('/todos/3')
    assert r.status_code==204 and r.content==b''
    assert client.delete('/todos/3').status_code==404
    assert client.get('/todos/3').status_code==404
    assert client.post('/todos',json={'title':'Neu'}).json()['id']==4
