import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("Loading dataset...")

data = pd.read_csv("data/dataset.csv")

X = data[['feature1','feature2']]
y = data['label']

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print("Training model...")

model = RandomForestClassifier()
model.fit(X_train,y_train)

print("Creating model folder...")

os.makedirs("models",exist_ok=True)

print("Saving model...")

joblib.dump(model,"models/model.pkl")

print("Training completed successfully!")
