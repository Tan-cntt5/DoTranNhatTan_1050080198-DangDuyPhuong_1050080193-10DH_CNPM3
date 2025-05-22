import pandas as pd

# Định nghĩa kích thước mỗi phần
chunksize = 10000

# Khởi tạo các biến để lưu kết quả
summary = {'k=5': {'Rows': 0}, 'k=10': {'Rows': 0}}
differences = []

# Đọc và xử lý từng phần của adult_k5.csv và adult_k10.csv
k5_chunks = pd.read_csv('adult_k5.csv', chunksize=chunksize)
k10_chunks = pd.read_csv('adult_k10.csv', chunksize=chunksize)

for i, (k5_chunk, k10_chunk) in enumerate(zip(k5_chunks, k10_chunks), start=1):
    print(f"Đang xử lý phần {i}...")

    # Cập nhật số lượng dòng
    summary['k=5']['Rows'] += len(k5_chunk)
    summary['k=10']['Rows'] += len(k10_chunk)

    # So sánh từng phần và lưu các khác biệt
    diff = k5_chunk.compare(k10_chunk, align_axis=0)
    if not diff.empty:
        differences.append(diff)
        print(f"Phát hiện khác biệt trong phần {i}")

# Lưu kết quả tóm tắt
summary_df = pd.DataFrame(summary)
summary_df.to_csv('comparison_summary.csv')
print("Đã lưu tóm tắt vào comparison_summary.csv")

# Lưu các khác biệt
if differences:
    all_differences = pd.concat(differences)
    all_differences.to_csv('comparison_differences.csv')
    print("Đã lưu các khác biệt vào comparison_differences.csv")
else:
    print("Không có khác biệt nào được phát hiện.")

