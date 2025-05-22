#!/usr/bin/env python3
import pandas as pd
from phe import paillier

# 1) Sinh keypair Paillier
pubkey, privkey = paillier.generate_paillier_keypair()

# 2) Đọc dữ liệu cục bộ của mỗi “site”
dfA = pd.read_csv('adult_k10_14_partA.csv')
dfB = pd.read_csv('adult_k10_14_partB.csv')

# 3) Chọn tập item để tính support, ví dụ các giá trị của Workclass
items = sorted(dfA['Workclass'].unique().tolist() +
               dfB['Workclass'].unique().tolist())
items = list(dict.fromkeys(items))  # loại trùng

# 4) Mỗi bên tính local counts
countsA = dfA['Workclass'].value_counts().to_dict()
countsB = dfB['Workclass'].value_counts().to_dict()

# 5) Mỗi bên mã hóa counts với public key
encA = {item: pubkey.encrypt(countsA.get(item, 0)) for item in items}
encB = {item: pubkey.encrypt(countsB.get(item, 0)) for item in items}

# 6) “Aggregator” (có thể là một bên thứ ba) nhận ciphertext và cộng
encSum = {item: encA[item] + encB[item] for item in items}

# 7) Giải mã tổng để lấy global support
global_support = {item: privkey.decrypt(encSum[item]) for item in items}

# 8) Hiển thị kết quả
print("Global support (Workclass):")
for item, sup in global_support.items():
    print(f"  {item}: {sup}")
