import json

def fileWrite(Lista, direccion):

    with open(direccion, 'w') as f:
        f.write(json.dumps(Lista))
    

def fileRead(direccion):

    with open(direccion, 'r') as f:
        a = json.loads(f.read())
    return a
