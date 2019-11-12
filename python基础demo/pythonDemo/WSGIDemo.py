# WSGIDemo.py
def webFirstFuntion(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/templates')])
    return [b'<h1>Hello, web!</h1>']
