import numpy as np
import pandas as pd
from scipy import stats

#create a sample dataset
data = {
    'study_hours':[2,3,5,7,9,4,8,6,10,1],
    'exam_score':[55,68,72,81,93,65,88,76,98,50]
}
df = pd.DataFrame(data)

#2 Individual statistics using Pandas and numpy
x = df['study_hours']
mean_val = np.mean(x)
median_val = np.median(x)
variance = np.var(x)
std = np.std(x)
variance_val = np.var(x,ddof=1)
std_dev_val = np.std(x,ddof=1)
print(f"Mean:{mean_val}")
print(f"Median:{median_val}")
print(f"Variance:{variance}")
print(f"Standard Deviation:{std:.2f}")
print(f"Variance Variance:{variance_val:.2f}")
print(f"Standard Deviation Variance:{std_dev_val:.2f}")

#3 Correlation ( Pearson amd Spearmam)
person_corr , p_val = stats.pearsonr(df['study_hours'],df['exam_score'])
print(f"Pearson Correlation:{person_corr:.4f}")
print(f"P-value:{p_val:.4f}\n")

#4 Summary matrix using Pandas
print("-----Pandas Summary Statistics-----")
print(df.describe())

print("\n---------- Correlation Matrix ----------")
print(df.corr())