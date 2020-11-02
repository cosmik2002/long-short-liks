import pytest
from flask import url_for

TEST_URL = "http://ya.ru"
TEST_MALFORMED_URL = "delete * from links"
TEST_BAD_POSTFIX = "__bad__"
TEST_MISSED_POSTFIX = "99999"


@pytest.mark.usefixtures('client_class')
class TestSuite:

    def test_set_link(self):
        url = url_for('linksresource')
        resp = self.client.put(url, data={"long_url":TEST_URL})
        assert "short_link" in resp.json
        assert resp.status_code == 200

    def test_set_and_get_link(self):
        url = url_for('linksresource')
        resp = self.client.put(url, data={"long_url":TEST_URL})
        resp = self.client.get(resp.json['short_link'])
        assert resp.status_code == 302
        assert resp.headers['Location'] == TEST_URL

    def test_link_stat(self):
        url = url_for('linksresource')
        resp = self.client.put(url, data={"long_url":TEST_URL})
        short_postfix = resp.json['short_link'].split('/')[-1]
        short_link = resp.json['short_link']
        resp = self.client.get(url_for('linksstat', short_postfix=short_postfix))
        assert resp.json['count'] == 0
        resp = self.client.get(short_link)
        resp = self.client.get(url_for('linksstat', short_postfix=short_postfix))
        assert resp.json['count'] == 1

    def test_malformed_url(self):
        url = url_for('linksresource')
        resp = self.client.put(url, data={"long_url":TEST_MALFORMED_URL})
        assert resp.status_code == 400

    def test_bad_postfix(self):
        url = url_for('linksresource', short_postfix=TEST_BAD_POSTFIX)
        resp = self.client.get(url)
        assert resp.status_code == 400

    def test_missed_postfix(self):
        url = url_for('linksresource', short_postfix=TEST_MISSED_POSTFIX)
        resp = self.client.get(url)
        assert resp.status_code == 404