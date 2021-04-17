# Summary of 3_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 1
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

165.0 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.107123 | nan           |
| auc       | 0.98904  | nan           |
| f1        | 0.960627 |   0.644442    |
| accuracy  | 0.961882 |   0.644442    |
| precision | 1        |   0.999698    |
| recall    | 1        |   4.91496e-05 |
| mcc       | 0.925649 |   0.644442    |


## Confusion matrix (at threshold=0.644442)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   79921 |                     501 |
| Labeled as positive |                    5630 |                   74792 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

[<< Go back](../README.md)
