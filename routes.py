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
    'slug': '[a-z]+'
}


def dispatcher(url):
    print '---------------------------------------'
    url = url[1:]
    for p, view in urlpatterns:
        # additional for custom converter
        for c in CONVERTERS:
            p = re.sub( '<'+c+':(\w+>)', r'(?P<\1' + CONVERTERS[c] + ')', p)

        # check matching
        match = re.match(p, url);
        if match is None:
            continue

        print url, ' -> ', p
        print 'view:', view, match.groupdict()
        break


dispatcher('/test')
dispatcher('/articles/2003/')
dispatcher('/articles/2010/')
dispatcher('/articles/2010/20/')
dispatcher('/articles/2010/12/')
dispatcher('/articles/2010/12/test/')
dispatcher('/not-matching-goes-to-home')
