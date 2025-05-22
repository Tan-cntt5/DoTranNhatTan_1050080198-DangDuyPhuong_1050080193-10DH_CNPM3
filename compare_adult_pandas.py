import pandas as pd

# 1. Đọc hai file CSV
df_k5  = pd.read_csv('adult_k5.csv')
df_k10 = pd.read_csv('adult_k10.csv')

# 2. Tính bảng tóm tắt
summary = {
    'Rows': [
        len(df_k5),
        len(df_k10)
    ],
    'Unique_Age': [
        df_k5['Age'].nunique(),
        df_k10['Age'].nunique()
    ],
    'Unique_Native-country': [
        df_k5['Native-country'].nunique(),
        df_k10['Native-country'].nunique()
    ],
    'Suppressed_Age_%': [
        (df_k5['Age'] == '*').mean() * 100,
        (df_k10['Age'] == '*').mean() * 100
    ],
    'Suppressed_Native-country_%': [
        (df_k5['Native-country'] == '*').mean() * 100,
        (df_k10['Native-country'] == '*').mean() * 100
    ],
    'Mean_Hours-per-week': [
        df_k5['Hours-per-week'].mean(),
        df_k10['Hours-per-week'].mean()
    ],
    'Mean_Capital-gain': [
        df_k5['Capital-gain'].mean(),
        df_k10['Capital-gain'].mean()
    ]
}
df_summary = pd.DataFrame(summary, index=['k=5', 'k=10'])
df_summary.to_csv('comparison_summary.csv')
print("Saved summary to comparison_summary.csv")

# 3. So sánh chi tiết giá trị khác biệt
diff = df_k5.compare(df_k10, align_axis=0)
diff.to_csv('comparison_differences.csv')
print("Saved cell-wise diffs to comparison_differences.csv")

# 4. So sánh hàng tồn tại (merge indicator)
merged = pd.merge(
    df_k5, df_k10,
    on=['Age','Native-country'],
    how='outer',
    indicator=True
)
merged.to_csv('comparison_indicator.csv', index=False)
print("Saved merge indicator to comparison_indicator.csv")
