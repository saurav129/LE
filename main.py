import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import simpledialog, messagebox

# Generate random data
np.random.seed(42)
yoe = np.random.randint(0, 20, size=1000)
salaries = 30000 + (yoe * 2000) + np.random.randint(-5000, 5000, size=1000)

# Create a DataFrame
data = pd.DataFrame({'Years of Experience': yoe, 'Salary': salaries})

X = data[['Years of Experience']]
y = data['Salary']

feature_name = X.columns[0]

model = LinearRegression()
model.fit(X, y)

root = tk.Tk()
root.withdraw()
new_yoe = simpledialog.askinteger("Years of Experience", "Enter years of experience:")

# Predict the salary for the user's input
predicted_salary = model.predict([[new_yoe]])
messagebox.showinfo("Predicted Salary", f"The predicted salary is in $: {predicted_salary[0]:.2f}")