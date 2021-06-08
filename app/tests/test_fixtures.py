import pytest

@pytest.fixture
def empty_list():
    return []

def test_len_of_empty_list(empty_list):
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0

class FancyObject:
    def __init__(self):
        self.fancy = True
        print(f"\nFancyObject: {self.fancy}")

    def or_is_it(self):
        self.fancy = not self.fancy

    def cleanup(self):
        print(f"\ncleanup: {self.fancy}")

@pytest.fixture
def so_fancy():
    fancy_object = FancyObject()

    yield fancy_object

    fancy_object.cleanup()

def test_so_fancy(so_fancy):
    assert so_fancy.fancy
    so_fancy.or_is_it()
    assert not so_fancy.fancy