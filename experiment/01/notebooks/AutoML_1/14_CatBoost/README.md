# Summary of 14_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 8
- **rsm**: 1.0
- **loss_function**: Logloss
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
auc

## Training time

91.6 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.107882 | nan           |
| auc       | 0.988773 | nan           |
| f1        | 0.961166 |   0.607243    |
| accuracy  | 0.962262 |   0.607243    |
| precision | 1        |   0.999736    |
| recall    | 1        |   1.68561e-05 |
| mcc       | 0.925999 |   0.607243    |


## Confusion matrix (at threshold=0.607243)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   79656 |                     766 |
| Labeled as positive |                    5304 |                   75118 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

[<< Go back](../README.md)
