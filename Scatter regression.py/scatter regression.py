import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Give data 
income = np.array([5, 10, 20, 8, 4, 6, 12, 15])
pizza_sales = np.array([27, 46, 73, 40, 30, 28, 46, 59])

#scatter plot
plt.scatter (income,pizza_sales, color = 'blue', label = 'Data point')
plt.xlabel ("Average Income (1000$)")
plt.ylabel ("Pizza Sales (1000 pcs)")
plt. title ("Scatter Plot of Income vs. Pizza Sales ")
plt.legend()
plt.show()

# Linear regression 

slope, intercept, r_value, p_values, std_err = linregress(income, pizza_sales)
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"Correlation coefficient (R): {r_value}")
print(f"R-squared: {r_value**2}")

# Predication based on the regression line

y_pred = slope * income + intercept

# Compute SSR, SSE, SST

sst = np. sum(pizza_sales - np.mean (pizza_sales))**2 # Total sum of sqaure
ssr = np. sum(y_pred - np.mean (pizza_sales))**2 # Regression sum of sqaure 
sse = np. sum((pizza_sales - y_pred))**2 # Sum of sqaure errors

print(f"SSR (Regression Sum of Sqaure): {ssr}")
print(f"SSE (Sum of Sqaure Errors): {sse}")
print(f"SSR (Total Sum of Sqaures): {sst}")
print(f"R-Sqaured):{ssr/sst}")
