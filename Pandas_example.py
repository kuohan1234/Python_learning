import pandas as pd

# 建立 DataFrame
data = {
    "姓名": ["小明", "小華", "小美","a", "小明", "小華"],
    "分數": [88, 92, 79, 85, 90, 95]
}
df = pd.DataFrame(data)

# 顯示 DataFrame
print("原始資料：")
print(df)

# show the info of the DataFrame
print("\nDataFrame 資訊：")
print(df.info())

print(df.groupby("姓名").sum())
print(df.groupby("姓名").median())

K = df.groupby("姓名").mean()
print("\n每個人的平均分數：")
test = "Hello World"
print(f"KH format print : {test}")

test2 = "KH dont care about"

print(f"KH dont care about {test2}")







