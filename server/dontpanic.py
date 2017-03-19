import bottle
from bottle import route, get, post, request, run, template, static_file, error

from pprint import pprint

bottle.debug(True)

# Static Routes
@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="../client/static/css")

@get("/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="../client/static/font")

@get("/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="../client/static/img")

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="../client/static/js")

@get('/')
def root():
    return static_file('index.html', root='../client/static')

@post('/')
def root():
    print "Wisdom: ", request.forms.get("wisdom")
    print "URL: ", request.forms.get("url")

    return static_file('confirmed.html', root='../client/static')

@route('/dontpanic/oblique')
def get_oblique_strategy():
	testquote = "You have reached the end of the universe"
	return template('{{quote}}', quote=testquote)

@error(404)
def error404(error):
        return "Lost in translation"

run(server='paste', host='localhost', port=8080)

