import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

FILE_PATH = "../data/students.csv"


def load_data(path):
    """Load dataset with validation"""
    if not os.path.exists(path):
        print("Error: Dataset file not found.")
        return None

    try:
        data = pd.read_csv(path)

        required_cols = ["math score", "reading score", "writing score"]

        if not all(col in data.columns for col in required_cols):
            print("Error: Required columns missing.")
            return None

        return data.dropna()

    except Exception as e:
        print("Error reading dataset:", e)
        return None


def prepare_data(data):
    """Create target column PASS / FAIL"""

    data["average"] = (
        data["math score"] +
        data["reading score"] +
        data["writing score"]
    ) / 3

    data["result"] = np.where(data["average"] >= 40, 1, 0)

    return data


def train_model(data):
    """Train Logistic Regression model"""

    X = data[["math score", "reading score", "writing score"]]
    y = data["result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(max_iter=200)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    return model


def validate_marks(value):
    """Check marks between 0 and 100"""
    return 0 <= value <= 100


def get_prediction(model):
    """Take input from user"""

    try:
        print("\n--- Enter Student Marks ---")

        math = float(input("Math: "))
        reading = float(input("Reading: "))
        writing = float(input("Writing: "))

        if not (validate_marks(math) and validate_marks(reading) and validate_marks(writing)):
            print("Marks must be between 0 and 100.")
            return

        sample = [[math, reading, writing]]

        result = model.predict(sample)

        if result[0] == 1:
            print("Prediction: PASS")
        else:
            print("Prediction: FAIL")

    except ValueError:
        print("Error: Enter numeric values only.")


def main():
    data = load_data(FILE_PATH)

    if data is None:
        print("Program stopped due to dataset error.")
        return

    data = prepare_data(data)

    model = train_model(data)

    get_prediction(model)


if __name__ == "__main__":
    main()