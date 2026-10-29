import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\JANVIER\Downloads\dataset.csv")

print(df.head())

correlation = (df.select_dtypes(include='number')).corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Between Numerical Variables")
plt.show()


result_counts = (
    df["exam_score"]
    .apply(lambda score: "Pass" if score >= 50 else "Fail")
    .value_counts()
)

result_counts.plot.pie(
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Pass and Fail Distribution")
plt.ylabel("")
plt.show()