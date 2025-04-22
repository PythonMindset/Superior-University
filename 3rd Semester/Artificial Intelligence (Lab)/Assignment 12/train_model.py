import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import pickle

df = pd.read_csv("dataset.csv")
for col in ['Open', 'High', 'Low', 'Close']:
    df[col] = df[col].fillna(df[col].mean())

df = df.drop(columns=['Volume', 'Date'], errors='ignore')

X = df[['Open', 'High', 'Low']]
y = df['Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = SVR()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")