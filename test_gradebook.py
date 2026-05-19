import pytest
from gradebook import GradeBook

class TestGradeBook:
    # 1. pre-populated GradeBook used in at least 2 tests
    def test_average(self, populated_gradebook):
        # (95 + 82 + 76 + 65 + 50) / 5 = 73.6
        assert populated_gradebook.average() == pytest.approx(73.6)

    def test_highest(self, populated_gradebook):
        assert populated_gradebook.highest() == 95

    def test_lowest(self, populated_gradebook):
        assert populated_gradebook.lowest() == 50

    # 3. parametrize overall five letter-grade boundaries
    @pytest.mark.parametrize("score, expected_grade", [
        (100, "A"),
        (90, "A"),
        (89.9, "B"),
        (80, "B"),
        (79.9, "C"),
        (70, "C"),
        (69.9, "D"),
        (60, "D"),
        (59.9, "F"),
        (0, "F")
    ])
    def test_letter_grade(self, score, expected_grade):
        gb = GradeBook()
        assert gb.letter_grade(score) == expected_grade

    # 4. A test asserting an out-of-range score raises ValueError
    def test_add_score_out_of_range(self):
        gb = GradeBook()
        with pytest.raises(ValueError):
            gb.add_score("InvalidHigh", 101)
            
        with pytest.raises(ValueError):
            gb.add_score("InvalidLow", -1)
            
    def test_letter_grade_out_of_range(self):
        gb = GradeBook()
        with pytest.raises(ValueError):
            gb.letter_grade(105)
