import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n", "^_^")
    yield
    print("\n", ":3")


@pytest.fixture()
def very_important_fixture():
    print("\n", ":)")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n", ":-Р")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass
    
    def test_second_smiling_faces(self, prepare_faces):
        pass
