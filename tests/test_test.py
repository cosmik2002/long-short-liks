import pytest
from flask import url_for


@pytest.mark.usefixtures('client_class')
class TestSuite:

    def test_set_link(self):
        url = url_for('linksresource')
        resp = self.client.put(url, data={"long_url":"http://ya.ru"})
        assert "short_link" in resp.json
        assert resp.status_code == 200

    def test_myview(self):
        url = url_for('linksresource', short_postfix="8")
        assert self.client.get(url).status_code == 302