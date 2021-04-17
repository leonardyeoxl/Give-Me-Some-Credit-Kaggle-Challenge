# Summary of 27_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: auc
- **num_leaves**: 95
- **learning_rate**: 0.2
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

93.5 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.107882 | nan           |
| auc       | 0.9895   | nan           |
| f1        | 0.960873 |   0.549875    |
| accuracy  | 0.961913 |   0.549875    |
| precision | 1        |   0.998281    |
| recall    | 1        |   0.000262993 |
| mcc       | 0.925137 |   0.549875    |


## Confusion matrix (at threshold=0.549875)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   79498 |                     924 |
| Labeled as positive |                    5202 |                   75220 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

[<< Go back](../README.md)
