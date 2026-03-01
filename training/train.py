"""
Flow A - Training Pipeline
Dataset: California Housing
"""
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
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

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("n\Data Types")
    print(df.dtypes)

    print("\nBasics Statistics:")
    print(df.describe())


    #separate features and target
    X = df.drop("target", axis=1)
    Y = df["target"]

    print("\nFeature shape (X):", X.shape)
    print("Target shape (Y):", Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,Y, test_size=0.2, random_state=42
    )

    print("\nTraining set shape:", X_train.shape)
    print("\nTest set shape:", X_test.shape)



if __name__ == "__main__":
    main()