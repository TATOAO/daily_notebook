``` py
# to csv

df.to_csv("filename.csv", encoding="utf-8-sig")
## encoding - 解决导出中文解码问题



# to json
test_data.to_json('test.json', orient="records", force_ascii=False)
## force_ascii - 解决导出中文解码问题

```