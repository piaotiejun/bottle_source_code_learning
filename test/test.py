#!/usr/bin/python
#coding=utf8

from bottle import Bottle, run, DictProperty, request

app = Bottle()
catchall = DictProperty('config', 'catchall')
print('========')
print(catchall)
print(dir(catchall))
print(catchall.__dict__)
print('========')

@app.route(path='/hello', method=['POST'], )
def hello():
    arg = request.forms.get('name', 'piao')
    return "Hello %s!"%(arg)

def hellos():
    return "Hello Worlds!"
app.route(path='/hellos', method=['GET'], callback=hellos)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=10000, reloader=True)

