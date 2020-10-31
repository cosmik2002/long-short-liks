import pytest
from links_transform import create_app

@pytest.fixture
def app():
    app = create_app()
    return app