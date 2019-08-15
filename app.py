from logging import warning
from natrix import app, route
from google.appengine.api import urlfetch


app.config['session-key'] = 'a8e423319c7788900e4f415f8d283a28'
API_KEY = 'a23d75001f4a4f37a42b1c41bb2abc10'


@route('/')
def home(x):
    version = 8
    x.render('index.html', version=version)


@route('/api/#load')
def get_new(x):
    page = x.request['page'] or 0
    url = 'https://newsapi.org/v2/everything?q=google'
    url = '%s&apiKey=%s&pageSize=12&page=%s' % (url, API_KEY, page)

    result = urlfetch.fetch(url=url, method=urlfetch.GET)
    x.response.code = result.status_code
    x.response(result.content, encode='json')


@route(':error-404')
def error_404(x):
    x.response.code = 404
    warning('Not found: %s' % x.request.url)
    x.response('Page Node Found')
