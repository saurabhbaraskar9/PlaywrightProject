import pytest


@pytest.fixture(scope = 'module')
def prework ():
    print("I setup instance.")

@pytest.fixture(scope = 'module')
def secondCheck():
    print("I validate pre-conditions")
    yield
    print("I validate post-conditions.")


def test_mainCheck(prework,secondCheck):
    print("This is first test.")