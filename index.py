from bottle import route, run, template

@route('/')
def index():
  return 'Bottle sample'

run(host='localhost', port=8080, debug=True)
