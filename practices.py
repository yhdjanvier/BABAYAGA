import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.linear_model import LinearRegression
dt = pd.read_csv("dataset.csv")
print(dt)
#print (dt.isnull().sum())
print (dt.duplicated().sum())
# plt.scatter(dt["exam_score"],dt["study_hours"])
# plt.show()

# Change Peter's exam score to 40
dt.loc[dt["student_name"] == "Peter", "exam_score"] = 460
# Delete the attendance column

# Save the changed dataset to a new CSV file
#dt.to_csv("updated1.csv",index=False)
dt.rename(columns={'exam_score':'exam_mark'},inplace=True)
print(dt)
