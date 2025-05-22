import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Đọc dữ liệu ẩn danh
df = pd.read_csv('adult_k10_14.csv')

# 2. Chọn các thuộc tính dạng categorical để mining
#    (ví dụ: workclass, education, marital-status, occupation, sex, native-country, income)
cats = ['Workclass','Education','Marital-status','Occupation','Relationship','Race','Sex','Native-country','Income']
df_cat = df[cats].astype(str)

# 3. One-hot encoding
df_ohe = pd.get_dummies(df_cat)

# 4. Apriori để tìm frequent itemsets với min support 0.05
frequent_itemsets = apriori(df_ohe, min_support=0.05, use_colnames=True)

# 5. Sinh association rules với min confidence 0.6
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# 6. Lưu kết quả
rules.to_csv('adult_k10_rules.csv', index=False)
print("Đã lưu luật vào adult_k10_rules.csv")
