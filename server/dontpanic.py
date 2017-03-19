from bottle import route, get, run, template, static_file, error

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

@route('/')
def root():
        return static_file('index.html', root='../client/static')

@route('/dontpanic/oblique')
def get_oblique_strategy():
	testquote = "You have reached the end of the universe"
	return template('{{quote}}', quote=testquote)

@error(404)
def error404(error):
        return "Lost in translation"

run(server='paste', host='localhost', port=8080)

