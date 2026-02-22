import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "../data/marks.csv"

# Load Dataset
def load_data(file_path):
  
    # Check file existence
    if not os.path.exists(file_path):
        print("Error: Dataset file not found.")
        return None

    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print("Error reading CSV file:", e)
        return None

    # Validate required columns
    required_columns = ["Name", "Marks"]
    for col in required_columns:
        if col not in data.columns:
            print(f"Error: Column '{col}' not found in dataset.")
            return None
    data["Marks"] = pd.to_numeric(data["Marks"], errors="coerce")

    #  used to Removes invalid rows
    data = data.dropna(subset=["Marks"])

    if data.empty:
        print("Error: No valid marks data found.")
        return None

    return data


# Analyze Marks
def analyze_marks(data):
    """
     it is used to Calculate average, highest and lowest marks.
    """

    print("\n----- Student Marks Dataset -----")
    print(data)

    # Average
    average_marks = data["Marks"].mean()
    print("\nAverage Marks:", round(average_marks, 2))

    # Highest scorer
    highest = data.loc[data["Marks"].idxmax()]
    print("\nHighest Scorer:")
    print("Name:", highest["Name"])
    print("Marks:", highest["Marks"])

    # Lowest scorer
    lowest = data.loc[data["Marks"].idxmin()]
    print("\nLowest Scorer:")
    print("Name:", lowest["Name"])
    print("Marks:", lowest["Marks"])
# Bar Chart
def plot_bar_chart(data):
    """
    Generate bar chart for student marks.
    """
    plt.figure()
    plt.bar(data["Name"], data["Marks"])
    plt.title("Student Marks Bar Chart")
    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_histogram(data):
    """
    Generate histogram for marks
    """
    plt.figure()
    plt.hist(data["Marks"], bins=5)
    plt.title("Marks Distribution Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()
# Main Function
def main():
    data = load_data(FILE_PATH)

    if data is None:
        print("Program stopped due to dataset error.")
        return

    analyze_marks(data)
    plot_bar_chart(data)
    plot_histogram(data)


# Program Entry Point
if __name__ == "__main__":
    main()