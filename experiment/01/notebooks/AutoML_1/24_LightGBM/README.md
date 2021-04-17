# Summary of 24_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: auc
- **num_leaves**: 95
- **learning_rate**: 0.1
- **feature_fraction**: 1.0
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 30
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
auc

## Training time

146.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.106463 | nan           |
| auc       | 0.98983  | nan           |
| f1        | 0.961073 |   0.388503    |
| accuracy  | 0.961764 |   0.598877    |
| precision | 1        |   0.999581    |
| recall    | 1        |   0.000339707 |
| mcc       | 0.925256 |   0.598877    |


## Confusion matrix (at threshold=0.598877)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   79803 |                     619 |
| Labeled as positive |                    5531 |                   74891 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

[<< Go back](../README.md)
