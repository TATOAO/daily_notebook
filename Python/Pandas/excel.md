
# excel 日期问题

[Link](https://www.edureka.co/community/207831/convert-column-excel-format-ddddd-tttt-datetime-using-pandas ":)")

```py
s_int = s.astype(int)
# Correcting Excel Leap Year bug.
days = pd.to_timedelta(np.where(s_int > 59, s_int - 1, s_int), unit='D')
secs = pd.to_timedelta(
    ((s - s_int) * 86400.0).round().astype(int), unit='s')

pd.to_datetime('1899/12/31') + days + secs

0   2016-02-11
1   2017-01-19
dtype: datetime64[ns]

```

