import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("menu.csv")
print(df.info())
df["fat_calorie_ratio"] = df["Calories from Fat"] / df["Calories"]
temp = df[["Item", "fat_calorie_ratio"]].sort_values(by="fat_calorie_ratio", ascending=False)
print(temp)
temp_sugars=df.sort_values(by="Sugars", ascending=False)[["Item", "Sugars"]]
print(temp_sugars)
df["protein_density"] = np.where(df["Calories"] > 0, df["Protein"]/df["Calories"],np.nan)
temp_proteins=df.sort_values(by="protein_density", ascending=False)[["Item", "protein_density"]]
print(temp_proteins)
df["Unhealthy_score"] = (df["Total Fat (% Daily Value)"] + df["Sodium (% Daily Value)"] + df["Sugars"])
temp_unhealthy=df.sort_values(by="Unhealthy_score", ascending=False)
print(temp_unhealthy)
temp_iron=df[["Item", "Iron (% Daily Value)"]].sort_values(by="Iron (% Daily Value)", ascending=False)
print(temp_iron)
df["Vitamins"]=df["Vitamin A (% Daily Value)"] + df["Vitamin C (% Daily Value)"]
temp_vitamins=df.sort_values(by="Vitamins", ascending=False)
print(temp_vitamins)
df["health_score"] = (
# Good nutrients
df["Protein"] * 2 +
df["Dietary Fiber"] * 2 +
df["Vitamin A (% Daily Value)"] +
df["Vitamin C (% Daily Value)"] +
df["Calcium (% Daily Value)"] +
df["Iron (% Daily Value)"]

# Bad nutrients (penalty)
- df["Saturated Fat (% Daily Value)"] * 2
- df["Sodium (% Daily Value)"] * 2
- df["Sugars"]
)
temp_health=df.sort_values(by="health_score", ascending=False)[
    ["Item", "Category", "health_score"]
].head(10)

print(temp_health)

temp_health_plot = temp_health.sort_values(by="health_score", ascending = True)

plt.figure(figsize=(12, 7))
plt.barh(temp_health_plot["Item"], temp_health_plot["health_score"], color="#2ecc71")
plt.xlabel("Health Score", fontsize=12, fontweight="bold")
plt.ylabel("Menu Item", fontsize=12, fontweight="bold")
plt.title("Top 10 Healthiest McDonald's Menu Items", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df["Total Fat"], df["Sugars"], c=df["Calories"], cmap="Reds", alpha=0.6, edgecolors='k')
plt.colorbar(scatter, label="Total Calories")
plt.title("Relationship Between Total Fat, Sugars, and Calories", fontsize=14, fontweight="bold")
plt.xlabel("Total Fat (g)", fontsize=12)
plt.ylabel("Sugars (g)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df["Sugars"], bins=20, edgecolor="black")
plt.xlabel("Sugar (g)")
plt.ylabel("Number of Items")
plt.title("Distribution of Sugar Content in McDonald's Menu")
plt.tight_layout()
plt.show()

top_calories = df.nlargest(10, 'Calories')
plt.figure(figsize=(10, 6))
plt.barh(top_calories['Item'], top_calories['Calories'])
plt.xlabel("Calories")
plt.ylabel('Item')
plt.title("Top 10 Highest-Calorie McDonald's Items")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 7))
df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap="Paired")

plt.title("Distribution of Items by Category")
plt.ylabel('')
plt.show()

plt.figure(figsize=(10, 7))
plt.hist(df['Vitamins'], bins=30, edgecolor='black')
plt.xlabel("Vitamin Distribution", fontsize=12, fontweight='bold')
plt.ylabel("Number of Item", fontsize=12, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Distribution of Vitamins Across McDonald's Menu", fontsize=16, fontweight='bold')

plt.show()

categories = df["Category"].unique() 
sodium_data = [df[df['Category'] == category]['Sodium'] for category in categories]

plt.figure(figsize=(12, 6))
plt.boxplot(sodium_data, tick_labels=categories)
plt.xticks(rotation=45)
plt.ylabel("Sodium (mg)")
plt.title("Sodium Distribution by McDonald's Items")
plt.tight_layout()
plt.show()

#plt.figure(figsize-(12, 6))
#plt.barh()
#plt.xlabel()
#plt.ylabel()
#plt.grid(True, linestyle="--", alpha=0.5)
#plt.title("Happy Meal Contents Compared To Other McDonald's Items", fontsize=16, fontweight='bold')
