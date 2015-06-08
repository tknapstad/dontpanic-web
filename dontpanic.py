from bottle import route, run, template

#@route('/dontpanic/<name>')
#def index(name):
#    return template('<b>Hello {{name}}</b>!', name=name)

@route('/dontpanic')
def welcome():
	return '<b>Welcome</b>'

@route('/dontpanic/oblique')
def get_oblique_strategy():
	testquote = "You have reached the end of the universe"
	return template('{{quote}}', quote=testquote)

#run(server='cherrypy', host='10.25.1.20', port=8080)
run(server='cherrypy', host='localhost', port=8080)

