import numpy as np    

#Sample Data in Excel Example
#e = np.array([-1.70, -1.75, -1.87, -2.00, -2.14, -2.30]) # Price Elasticities
#bp = np.array([4.1, 2.3, 3.2, 4.5, 10.1, 5.4]) # Item Current Prices
#bq = np.array([100, 120, 340, 50, 25, 150]) # Item Baseline Forecast
#Constraints
#price_change = 0.2 # Constraint: Maximum % Price Change allowed per Item
#budget = 300 # Constraint: Maximum Budget Available

# Simulated Data
item_count=10
bq = np.random.randint(50, 500, size=item_count) # Item Baseline Forecast
bp = np.random.randint(5, 10, size=item_count) + np.random.rand(item_count)  # Item Current Prices
e = 3 * np.random.rand(item_count) - 3 # Price Elasticities
budget = 0.1*np.dot(bp,bq) # Constraint: Maximum Budget Available
price_change = 0.2 # Constraint: Maximum % Price Change allowed per Item

