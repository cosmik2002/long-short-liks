import pytest
from flask import url_for


@pytest.mark.usefixtures('client_class')
class TestSuite:

    def test_myview(self):
        assert self.client.get(url_for('linksresource')).status_code == 200