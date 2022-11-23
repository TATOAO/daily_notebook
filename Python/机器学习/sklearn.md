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

```
