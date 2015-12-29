#!/usr/bin/python

from threading import current_thread
from bottle import Bottle, run, DictProperty

app = Bottle()
catchall = DictProperty('config', 'catchall')
print('========')
print(catchall)
print(dir(catchall))
print(catchall.__dict__)
print('========')

@app.route(path='/hello', method=['GET'], )
def hello():
    return "Hello World!"

def hellos():
    return "Hello Worlds!"
app.route(path='/hellos', method=['GET'], callback=hellos)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, reloader=True)

