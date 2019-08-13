# coding: utf-8
import pytest


def setup():
    pass


@pytest.fixture
def testbed():
    from google.appengine.ext.testbed import Testbed

    # create an instance of testbed class
    testbed = Testbed()

    # activate the testbed, which prepares the services stub for use
    testbed.activate()
    testbed.setup_env(app_id='debug', overwrite=True)

    # declare which stubs want to use
    testbed.init_search_stub()
    testbed.init_urlfetch_stub()

    return testbed


# tests
def test_index(testbed):
    import app
    import webtest
    testapp = webtest.TestApp(app.app)

    r = testapp.get('/')
    assert r.status_int == 200


def test_404(testbed):
    import app
    import webtest
    testapp = webtest.TestApp(app.app)
    params = {'page': '1'}

    assert testapp.get('/api/', expect_errors=True).status_int == 404
    assert testapp.post('/api/', params, expect_errors=True).status_int == 404


def test_api(testbed):
    import app
    import webtest
    testapp = webtest.TestApp(app.app)

    params = {':method': 'load', 'page': '1'}
    testapp.post('/api/', params).status_int == 200

    params = {':method': 'load'}
    assert testapp.post('/api/', params, expect_errors=True).status_int == 400

    params = {':method': 'load', 'page': '100000'}
    assert testapp.post('/api/', params, expect_errors=True).status_int == 426


if __name__ == '__main__':
    argv = [
        __file__,
        '-p', 'no:cacheprovider',  # disable cache
        '--quiet',                 # disable verbose report
        '--exitfirst',             # stop/exit on first fail
        '--capture=no',            # `print` immediately.
        '--color=auto',            # if possible show colorful output
    ]
    pytest.main(argv)
