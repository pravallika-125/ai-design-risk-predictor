import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("data.csv")

# Convert material to numeric
data["material"] = data["material"].map({"steel": 0, "aluminum": 1})

# Features and target
X = data[["length", "load", "material"]]
y = data["risk"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function
def predict_risk(length, load, material):
    material_map = {"steel": 0, "aluminum": 1}
    material_val = material_map[material]
    return model.predict([[length, load, material_val]])[0]
