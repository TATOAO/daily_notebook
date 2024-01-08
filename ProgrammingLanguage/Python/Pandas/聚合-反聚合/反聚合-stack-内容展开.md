

## Stack

### column里有list，展开成一个元素一行
``` py
s = df['label'].apply(lambda x: pd.Series(x.split("#"))).stack().reset_index(level=1, drop=True)
df.drop('label', axis=1).join(s)

#### 可能需要先设新的Series的名字
s = clean_bracket_df['用户意图'].apply(lambda x: pd.Series(re.split("[,，]", x))).stack().reset_index(level=1, drop=True)
stack_df = clean_bracket_df.join(s._set_name("用户意图2"))

```

