
# Report 

## Introduction
The objective of this report is to document the implementation and evaluation of a K-Nearest Neighbors (KNN) recommendation system for suggesting films using the MovieLens dataset. The KNN algorithm is implemented using the surprise library, and the analysis includes a detailed examination of the dataset, the advantages and disadvantages of the model, the training process, and the evaluation results.

## Data analysis
I did Explorative data analysis described in `notebooks/1.0. Data Exploration.ipynb`.

## Model Implementation
The KNN recommendation system is implemented using the surprise library. This implementation utilizes the user-item collaborative filtering approach. The code for model implementation can be found in the relevant scripts and modules.

# Model Advantages and Disadvantages
The KNN recommendation system has its strengths and weaknesses.

Advantages:

    * Simplicity and ease of implementation.
    * Effectiveness in capturing user preferences based on item similarities.

Disadvantages:

    * Scalability issues with large datasets.
    * Sensitivity to noise and outliers.
# Training Process
The training process involves preparing the dataset, splitting it into training and testing sets, and training the KNN model using collaborative filtering. The surprise library provides functionalities for these tasks.

## Evaluation
Evaluation metrics such as Mean Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) are crucial for assessing the performance of the recommendation system. These metrics are calculated using the benchmark/evaluate.py script. The surprise library's cross-validation is employed to obtain robust and unbiased performance scores.

## Results

The scores I got using 5 folds cross-validation: 
|                | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean    | Std     |
|----------------|--------|--------|--------|--------|--------|---------|---------|
| RMSE (testset) | 0.9781 | 0.9676 | 0.9711 | 0.9816 | 0.9719 | 0.9741  | 0.0051  |
| MAE (testset)  | 0.7728 | 0.7638 | 0.7666 | 0.7742 | 0.7700 | 0.7695  | 0.0038  |
| Fit time       | 0.48   | 0.52   | 0.43   | 0.40   | 0.42   | 0.45    | 0.05    |
| Test time      | 3.51   | 3.17   | 2.37   | 2.40   | 2.35   | 2.76    | 0.49    |
Mean RMSE: 0.9740637658805241
Mean MAE: 0.7694671102576232