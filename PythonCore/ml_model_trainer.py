import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

INPUT_FILE = "Reports/all_results.csv"
MODEL_FILE = "Models/strategy_classifier.pkl"

def extract_features(df):
    # Create target label: profitable = 1 if profit > threshold
    df["label"] = df["profit"] > 100  # Define your profitability threshold here

    # Drop strategy name (can be parsed later)
    X = df[["drawdown", "winrate", "trades"]]
    y = df["label"].astype(int)

    return X, y

def train_model():
    df = pd.read_csv(INPUT_FILE)
    X, y = extract_features(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    joblib.dump(model, MODEL_FILE)
    print(f"Model saved to {MODEL_FILE}")

if __name__ == "__main__":
    train_model()
