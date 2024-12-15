#### Precision - Recall Curve PR-曲线

[Official Sklearn package](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html ":)")


```py

from sklearn.metrics import PrecisionRecallDisplay

display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC"
)
_ = display.ax_.set_title("2-class Precision-Recall curve")


### RECOMMAND THIS WAY ####

y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(y_test, y_score, name="LinearSVC")
_ = display.ax_.set_title("2-class Precision-Recall curve")


```


## metric

#### roc auc

``` py

import sklearn

sklearn.metrics.roc_auc_score(true_y, prod_y)


display = metrics.plot_roc_curve(model, dataX, dataY)
_ = display.ax.set_title(taskname)

plt.savefig('plotname.png')

```

#### ROC 多个 roc曲线画在一起

```py

from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

plt.figure(0).clf()

pred = np.random.rand(1000)
label = np.random.randint(2, size=1000)
fpr, tpr, thresh = metrics.roc_curve(label, pred)
auc = metrics.roc_auc_score(label, pred)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))

pred = np.random.rand(1000)
label = np.random.randint(2, size=1000)
fpr, tpr, thresh = metrics.roc_curve(label, pred)
auc = metrics.roc_auc_score(label, pred)
plt.plot(fpr,tpr,label="data 2, auc="+str(auc))

plt.legend(loc=0)

```
[SO](https://stackoverflow.com/questions/42894871/how-to-plot-multiple-roc-curves-in-one-plot-with-legend-and-auc-scores-in-python ":)")

