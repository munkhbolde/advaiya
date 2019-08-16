import re


urlpatterns = [
   ('articles/2003/', 'views.special_case_2003'),
   (r'^articles/(?P<year>[0-9]{4})/$', 'views.year_archive'),
   (r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', 'views.month_archive'),
   (r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', 'views.article_detail'),
   ('articles/<int:year>/', 'views.year_archive'),
   (r'', 'home.as_view()'),
]

CONVERTERS = {
    'int': '[0-9]+',
    'slug': '[a-z]+',
}


def converter(pattern):
    for con in CONVERTERS:
        pattern = re.sub('<' + con + ':(\\w+>)', r'(?P<\1' + CONVERTERS[con] + ')', pattern)
    return pattern


def dispatcher(url):
    print '---------------------------------------'
    url = url[1:]
    for pattern, view in urlpatterns:
        # used for converting custom converter
        pattern = converter(pattern)

        # checking pattern match
        match = re.match(pattern, url)
        if match is None:
            continue

        print url, ' -> ', pattern
        print 'view:', view, match.groupdict()
        return
    print 'URL Mismatch: ' + url


dispatcher('/test')
dispatcher('/articles/2003/')
dispatcher('/articles/2010/')
dispatcher('/articles/2010/year/archive')
dispatcher('/articles/2010/20/')
dispatcher('/articles/2010/12/')
dispatcher('/articles/2010/12/test/')
dispatcher('/not-matching-goes-to-home')
