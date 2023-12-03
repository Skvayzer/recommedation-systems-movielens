# Practical Machine Learning and Deep Learning - Assignment 2 - Movie Recommender System
## Constantine Smirnov, B20-RO-01
k.smirnov@innopolis.university

## Task description

A collaborative-approach recommender system based on KNN that suggests films
## Data Description

In this assignment you will use [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/) consisting user ratings to movies.

**General information about the dataset:**
* It consists of 100,000 ratings from 943 users on 1682 movies
* Ratings are ranged from 1 to 5
* Each user has rated at least 20 movies
* It contains simple demographic info for the users (age, gender, occupation, zip code)

**Detailed description of data files:**

| **File** | **Description** |
| -------- | --------------- |
| u.data | Full dataset of 100000 ratings by 943 users on 1682 items. Users and items are numbered consecutively from 1. The data is randomly ordered. This is a tab separated list of user id, item id, rating, and timestamp. The time stamps are unix seconds. |
| u.info | The number of users, items, and ratings in the u data set |
| u.item | Information about the items (movies). This is a tab separated list of movie id, movie title, release date, video release date, IMDB URL, and genres. The last 19 fields are genres and contain binary values. Movies can be of several genres at once. The movie ids are the ones used in u.data |
| u.genre | List of genres. |
| u.user | Demographic information about the users. This is a tab separated list of user id, age, gender, occupation, zip code. The user ids are the ones used in in u.data file. |
| u.occupation | List of occupations. |
| u1.base, u1.test, u2.base, u2.test, u3.base, u3.test, u4.base, u3.test, u5.base, u5.test | The data sets u1.base and u1.test through u5.base and u5.test are 80%/20% splits of the u data into training and test data. Each of u1, ..., u5 have disjoint test sets; this if for 5 fold cross validation (where you repeat your experiment with each training and test set and average the results). These data sets can be generated from u.data by mku.sh. |
| ua.base, ua.test, ub.base, ub.test | The data sets ua.base, ua.test, ub.base, and ub.test split the u data into a training set and a test set with exactly 10 ratings per user in the test set. The sets ua.test and ub.test are disjoint. These data sets can be generated from u.data by mku.sh. |
| allbut.pl | The script that generates training and test sets where all but n of a users ratings are in the training data |
| mku.sh | A shell script to generate all the u data sets from u.data. |

## Evaluation

Mean RMSE and Mean MAE are calculated in `benchmark/evaluate.py`
The scores I got using 5 folds cross-validation: 
                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    0.9781  0.9676  0.9711  0.9816  0.9719  0.9741  0.0051  
MAE (testset)     0.7728  0.7638  0.7666  0.7742  0.7700  0.7695  0.0038  
Fit time          0.48    0.52    0.43    0.40    0.42    0.45    0.05    
Test time         3.51    3.17    2.37    2.40    2.35    2.76    0.49    
Mean RMSE: 0.9740637658805241
Mean MAE: 0.7694671102576232
