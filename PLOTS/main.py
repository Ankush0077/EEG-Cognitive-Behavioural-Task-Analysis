import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

# Load data
beads = pd.read_csv('data/beads_data_with_conf_slope.csv')
schizo = pd.read_csv('data/Schizotypy.csv')

# Select relevant metrics
beads_metrics = [
    'PID',
    'dtd_15_85',
    'dtd_60_40',
    'decision_confidence_15_85',
    'decision_confidence_60_40',
    'first_conf_85_15',
    'last_conf_85_15',
    'first_conf_60_40',
    'last_conf_60_40',
    'conf_slope'
]
beads_sel = beads[beads_metrics]

# Merge datasets
df = pd.merge(beads_sel, schizo, on='PID', how='inner')
df = df.drop(columns=['PID'])

# Compute correlation and p-value matrices
cols = df.columns
corr_matrix = pd.DataFrame(index=cols, columns=cols, dtype=float)
pval_matrix = pd.DataFrame(index=cols, columns=cols, dtype=float)

for col1 in cols:
    for col2 in cols:
        corr, pval = pearsonr(df[col1], df[col2])
        corr_matrix.loc[col1, col2] = corr
        pval_matrix.loc[col1, col2] = pval

# Mask non-significant correlations (p >= 0.1)
significant_mask = (pval_matrix < 0.1) & (pval_matrix > 0)
filtered_corr = corr_matrix.where(significant_mask)

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(filtered_corr, annot=True, fmt='.2f', cmap='coolwarm', square=True, mask=~significant_mask)
plt.title('Significant Correlations (p < 0.1)')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
