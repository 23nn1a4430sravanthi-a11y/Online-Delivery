import pandas as pd

# ===== Step 1: Load Dataset =====
df = pd.read_csv("restaurants.csv")

# ===== Step 2: Check Online Delivery Column =====
# Column usually named 'Has Online delivery'
# Values are typically 'Yes' and 'No'

online_counts = df['Has Online delivery'].value_counts()

total_restaurants = len(df)

# Percentage calculation
online_percentage = (online_counts / total_restaurants) * 100

print("===== Percentage of Restaurants Offering Online Delivery =====")
for status, percent in online_percentage.items():
    print(f"{status}: {percent:.2f}%")

# ===== Step 3: Compare Average Ratings =====
avg_rating_online = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("\n===== Average Ratings Comparison =====")
print("With Online Delivery (Yes):", round(avg_rating_online['Yes'], 2))
print("Without Online Delivery (No):", round(avg_rating_online['No'], 2))

# ===== Step 4: Save Results =====
result = pd.DataFrame({
    "Online Delivery": online_percentage.index,
    "Percentage (%)": online_percentage.values,
    "Average Rating": avg_rating_online.values
})

result.to_csv("online_delivery_analysis.csv", index=False)

print("\nResults saved as 'online_delivery_analysis.csv'")
