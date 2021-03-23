from .fixtures import root
import pytest


@pytest.mark.root
def test_hello_ollivanders(root):
    assert b'{"hello": "Ollivanders"}' in root.data