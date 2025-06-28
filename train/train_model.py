from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib

# Cargar el dataset California Housing
data = fetch_california_housing()
X, y = data.data, data.target

# Separar datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, "california_housing_prediction.joblib")

print("✅ Trained model with California Housing and saved as california_housing_prediction.joblib")

