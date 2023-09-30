import sys
sys.path.append('../python-ci-cd')
from source.app import index


def test_index():
    assert index() == "Hello, World!"