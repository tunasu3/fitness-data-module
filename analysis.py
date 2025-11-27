import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# 1. LOAD DATA

df = pd.read_excel("fitness_data.xlsx")


df['Date'] = pd.to_datetime(df['Date'])

print("\n DATA SAMPLE \n")
print(df.head())



# 2. DESCRIPTIVE STATISTICS

print("\n DESCRIPTIVE STATISTICS\n")
print(df.describe())


# 3. TIME-SERIES PLOTS

plt.figure(figsize=(12,4))
plt.plot(df['Date'], df['Calories Burned'], marker='o')
plt.title("Calories Burned Over Time")
plt.xlabel("Date")
plt.ylabel("Calories Burned")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(df['Date'], df['Sleep Duration'], marker='o', color='green')
plt.title("Sleep Duration Over Time")
plt.xlabel("Date")
plt.ylabel("Sleep Duration (hours)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(df['Date'], df['Workout Duration'], marker='o', color='orange')
plt.title("Workout Duration Over Time")
plt.xlabel("Date")
plt.ylabel("Workout Duration (minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# 4. CORRELATION MATRIX + HEATMAP

numerical_df = df[['Workout Duration', 'Calories Burned', 'Sleep Duration']]
corr = numerical_df.corr()

print("\n CORRELATION MATRIX \n")
print(corr)

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()




# 5. SCATTER PLOTS

plt.scatter(df['Sleep Duration'], df['Calories Burned'], c='purple')
plt.title("Sleep Duration vs Calories Burned")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Calories Burned")
plt.tight_layout()
plt.show()


plt.scatter(df['Workout Duration'], df['Calories Burned'], c='red')
plt.title("Workout Duration vs Calories Burned")
plt.xlabel("Workout Duration (minutes)")
plt.ylabel("Calories Burned")
plt.tight_layout()
plt.show()


plt.scatter(df['Workout Duration'], df['Sleep Duration'], c='blue')
plt.title("Workout Duration vs Sleep Duration")
plt.xlabel("Workout Duration (minutes)")
plt.ylabel("Sleep Duration (hours)")
plt.tight_layout()
plt.show()




# 6. HYPOTHESIS TESTS


print("HYPOTHESIS TESTING\n")

# H1 — Sleep vs Calories (Pearson)
r, p = stats.pearsonr(df['Sleep Duration'], df['Calories Burned'])
print(f"H1 Sleep ↔ Calories: r={r:.3f}, p={p:.4f}")


# Create Workout Day column
df['Workout Day'] = df['Workout Duration'] > 0


# H2 — Calories: Workout Day vs Non-workout Day (t-test)
w = df[df['Workout Day']==True]['Calories Burned']
nw = df[df['Workout Day']==False]['Calories Burned']
t, p = stats.ttest_ind(w, nw, equal_var=False)
print(f"H2 Calories Workout vs Rest: t={t:.3f}, p={p:.4f}")


# H3 — Sleep: Workout Day vs Non-workout Day
w_sleep = df[df['Workout Day']==True]['Sleep Duration']
nw_sleep = df[df['Workout Day']==False]['Sleep Duration']
t, p = stats.ttest_ind(w_sleep, nw_sleep, equal_var=False)
print(f"H3 Sleep Workout vs Rest: t={t:.3f}, p={p:.4f}")


# H4 — ANOVA Calories Across Weekdays
df['Weekday'] = df['Date'].dt.day_name()
groups = [g['Calories Burned'].values for n, g in df.groupby('Weekday')]
F, p = stats.f_oneway(*groups)
print(f"H4 Calories by Weekday ANOVA: F={F:.3f}, p={p:.4f}\n")

print(" COMPLETE ")