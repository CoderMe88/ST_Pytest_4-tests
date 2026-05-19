import pytest
from gradebook import GradeBook

@pytest.fixture
def populated_gradebook():
    gb = GradeBook()
    gb.add_score("Alice", 95)
    gb.add_score("Bob", 82)
    gb.add_score("Charlie", 76)
    gb.add_score("David", 65)
    gb.add_score("Eve", 50)
    return gb

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: mark test as slow to run"
    )
