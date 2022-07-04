from sanic import Sanic
from sanic.response import json
app = Sanic(name='servidor do fernandin')


@app.get('/home')
async def index(request):
    print("0.0.0.0:3000/home")
    return json({
        'status':True,
        'message':'Bem vindo ao servidor do fernandin'
    })


app.run(host='0.0.0.0',workers=4, port=3000)
