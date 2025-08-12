import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_excel("large_cyber_dataset.xlsx")

X = df.drop(columns=[
    'Flow_ID', 'Source_IP', 'Source_Port', 'Destination_IP',
    'Destination_Port', 'Timestamp', 'Label'
])

y = (df['Label'] != 'BENIGN').astype(int)
X = pd.get_dummies(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Model trained")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

joblib.dump(model, "model.h5")
print("Model saved as model.h5")