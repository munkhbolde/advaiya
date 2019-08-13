# coding: utf-8
import pytest


def setup():
    import pathfix  # noqa: #F401 (imported but unused)


@pytest.fixture
def testbed():
    from google.appengine.ext.testbed import Testbed

    # create an instance of testbed class
    testbed = Testbed()

    # activate the testbed, which prepares the services stub for use
    testbed.activate()
    testbed.setup_env(app_id="debug", overwrite=True)

    # declare which stubs want to use
    testbed.init_search_stub()
    testbed.init_urlfetch_stub()

    return testbed


# tests
def test_index(testbed):
    import app
    import webtest
    testapp = webtest.TestApp(app.app)

    r = testapp.get("/")
    assert r.status_int == 200

def test_api(testbed):
    params = {":method": "load", "page": "1"}
    assert testapp.post("/api/", params).status_int == 200

    params = {":method": "load"}
    assert testapp.post("/api/", params).status_int == 400

    params = {":method": "load", "page": "1000"}
    assert testapp.post("/api/", params).status_int == 429

if __name__ == "__main__":
    argv = [
        __file__,
        "-p", "no:cacheprovider",  # disable cache
        "--quiet",                 # disable verbose report
        "--exitfirst",             # stop/exit on first fail
        "--capture=no",            # `print` immediately. (useful for debugging)
        "--color=auto",            # if possible show colorful output
    ]
    pytest.main(argv)
