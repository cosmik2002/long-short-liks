import pytest
from flask import url_for

@pytest.mark.usefixtures('live_server')
class TestLiveServer:

    def test_server_is_up_and_running(self):
        res = urllib2.urlopen(url_for('index', _external=True))
        assert b'OK' in res.read()
        assert res.code == 200

    def test_passing(self):
        assert (1, 2, 3) == (1, 2, 3)