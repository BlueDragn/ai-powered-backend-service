"""
Flow A - Training Pipeline
Dataset: California Housing
"""
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

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
    print("\nTarget shape (Y):", Y.shape)

#Train/Test Split
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,Y, test_size=0.2, random_state=42
    )

    print("\nTraining set shape:", X_train.shape)
    print("\nTest set shape:", X_test.shape)
    #Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("Scaled training shape:", X_train_scaled.shape)
    print("Scaled test shape:", X_test_scaled.shape)

    #Train model
    model = LinearRegression()
    model.fit(X_train_scaled, Y_train)

    #Prediction
    Y_pred = model.predict(X_test_scaled)

    #Evaluation
    r2 = r2_score(Y_test, Y_pred)
    mse = mean_squared_error(Y_test, Y_pred)

    print("\nModel Performance:")
    print("R2 Score:", r2)
    print("MSE:", mse)



if __name__ == "__main__":
    main()