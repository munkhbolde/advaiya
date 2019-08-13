from logging import warning
from natrix import app, route


app.config['session-key'] = 'a8e423319c7788900e4f415f8d283a28'


@route('/')
def home(x):
    x.render('index.html')

@route(':error-404')
def error_404(x):
    x.response.code = 404
    warning('Not found: %s' % x.request.url)
    x.response('Page Node Found')
