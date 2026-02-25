"""
Flow A - Training Pipeline
Dataset: California Housing
"""
from sklearn.datasets import fetch_california_housing
def main():
    print("Loading California Housing dataset... ")
    data = fetch_california_housing()

    print("Dataset loaded successfully.")
    print("Feature shape:", data.data.shape)
    print("Target shape", data.target.shape)

if __name__ == "__main__":
    main()