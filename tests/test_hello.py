from peweb.src.main import route_pages

def test_hello():
    assert route_pages() == 'Hello World! It\'s totally radical, home'

