"""
Flow A - Training Pipeline
Dataset: California Housing
"""
from sklearn.datasets import fetch_california_housing
import pandas as pd

def main():
    print("Loading California Housing dataset... ")
    data = fetch_california_housing()

    #Convert to DataFrame
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["target"] = data.target


    print("\nDataset Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())

if __name__ == "__main__":
    main()