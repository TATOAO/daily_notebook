

# model load and model save 

save model method

```py

lgbr = lightgbm.LGBMRegressor(num_estimators = 200, max_depth=5)
lgbr.fit(train[num_columns], train["prep_time_seconds"])
preds = lgbr.predict(predict[num_columns])
lgbr.booster_.save_model('lgbr_base.txt')

model = lightgbm.Booster(model_file='lgbr_base.txt')
model.predict(predict[num_columns])
```

注意，如果是classfier， 重新加载的model不会有  predict_proba 的方法，
它只有predict() 这个方法，返回的结果就是:predict_proba 为1 的结果 

```py

model.predict_proba(testX)[:,1]
# 等价于
load_model.predict(testX)

```
