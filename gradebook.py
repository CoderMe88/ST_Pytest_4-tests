class GradeBook:
    def __init__(self):
        self.scores = {}

    def add_score(self, name: str, score: float):
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.scores[name] = score

    def average(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def highest(self) -> float:
        if not self.scores:
            return 0.0
        return max(self.scores.values())

    def lowest(self) -> float:
        if not self.scores:
            return 0.0
        return min(self.scores.values())

    def letter_grade(self, score: float) -> str:
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
