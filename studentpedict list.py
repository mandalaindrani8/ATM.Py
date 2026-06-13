# Student Pass/Fail Prediction

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample student data
# [Study Hours, Attendance Percentage]
X = [
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [1, 50],
    [2, 55],
    [9, 95]
]

# Target values
# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1, 1, 0, 0, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))

# Predict a new student
study_hours = 6
attendance = 78

result = model.predict([[study_hours, attendance]])

if result[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")