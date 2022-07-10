import pytest
import app
from controllers import topics

@pytest.fixture
def api(monkeypatch):
    test_Articulate_db={
        'person':['MJ','King Arthur'],
        'world':['Paris','The Thames'],
        'object':['Fan','Trident'],
        'action':['jump','sing'],
        'nature':['Zebra','Leaf'], 
    }

    monkeypatch.setattr(topics, "Articulate_db", test_Articulate_db)
    api = app.app.test_client()
    return api  