# PythonCore/ai_module.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_ai_model(results_csv):
    df = pd.read_csv(results_csv)
    X = df[["profit", "drawdown", "winrate"]]
    y = (df["profit"] > 0) & (df["drawdown"] < 20)  # Label: successful strategy

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Model accuracy: {acc:.2f}")
    return model

def predict_success(model, strategy_metrics):
    return model.predict([strategy_metrics])[0]
