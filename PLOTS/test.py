import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 0) Prepare output directory
out_dir = 'analysis-significant'
os.makedirs(out_dir, exist_ok=True)

# 1) Load & merge
beads = pd.read_csv('data/beads_data_with_conf_slope.csv')
schizo = pd.read_csv('data/Schizotypy.csv')

beads_metrics = [
    'dtd_15_85', 'dtd_60_40',
    'decision_confidence_15_85', 'decision_confidence_60_40',
    'first_conf_85_15', 'last_conf_85_15',
    'first_conf_60_40', 'last_conf_60_40',
    'conf_slope'
]
schizo_metrics = ['olife_total', 'ss1', 'ss2', 'ss3', 'ss4']

# Merge on PID, then drop it
df = pd.merge(
    beads[['PID'] + beads_metrics],
    schizo[['PID'] + schizo_metrics],
    on='PID', how='inner'
).drop(columns=['PID'])

# 2) Compute full corr & p‐value matrices
cols = df.columns
corr_mat = pd.DataFrame(index=cols, columns=cols, dtype=float)
pval_mat = pd.DataFrame(index=cols, columns=cols, dtype=float)

for x in cols:
    for y in cols:
        r, p = pearsonr(df[x], df[y])
        corr_mat.loc[x, y] = r
        pval_mat.loc[x, y] = p

# Save full matrices
corr_mat.to_csv(os.path.join(out_dir, 'full_corr_matrix.csv'))
pval_mat.to_csv(os.path.join(out_dir, 'full_pval_matrix.csv'))

# 3) Build significance mask (all pairs, same‐ and cross‐dataset)
sig_mask = (pval_mat < 0.05) & (pval_mat > 0)

# 4) Plot heatmap of all significant correlations
filtered_all = corr_mat.where(sig_mask)

plt.figure(figsize=(12, 10))
sns.heatmap(
    filtered_all,
    annot=True, fmt='.2f',
    cmap='coolwarm', square=True,
    mask=~sig_mask
)
plt.title('All Significant Correlations (p < 0.1)')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'all_sig_corr_heatmap.png'))
plt.close()

# 5) Now plot only cross‐dataset pairs individually
#    (schizotypy on x‐axis, beads on y‐axis)
cross_mask = pd.DataFrame(False, index=cols, columns=cols)
for b in beads_metrics:
    for s in schizo_metrics:
        cross_mask.loc[b, s] = True
        cross_mask.loc[s, b] = True

final_mask = sig_mask & cross_mask

sns.set(style="whitegrid")
for b in beads_metrics:
    for s in schizo_metrics:
        if final_mask.loc[b, s]:
            plt.figure(figsize=(6, 5))
            # swap x and y here:
            sns.regplot(
                x=s, y=b, data=df,
                scatter_kws={'s': 50, 'alpha': 0.6},
                line_kws={'color': 'red'}
            )
            r = corr_mat.loc[b, s]
            p = pval_mat.loc[b, s]
            plt.title(f"{s} vs {b}\nr = {r:.2f}, p = {p:.3f}")
            plt.xlabel(s)  # schizotypy label on x‐axis
            plt.ylabel(b)  # beads label on y‐axis
            fname = f"{s}_vs_{b}.png".replace(' ', '_')
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, fname))
            plt.close()

print(f"All outputs saved in `{out_dir}/`")
