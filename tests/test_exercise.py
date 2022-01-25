import os


def test_exercise():

    with open(os.path.dirname(__file__) + "/../exercise.txt", "r") as f:
        contents = f.read()
        if contents.split() != ["Hello", "Mars!"]:
            raise ValueError(
                f"Expected 'Hello Mars!', got '{contents.strip()}'")
