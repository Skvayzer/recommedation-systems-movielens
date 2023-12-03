from surprise import Dataset, Reader
from surprise.model_selection import cross_validate
from surprise import KNNBasic
import pickle 
import os

# Load the MovieLens 100k dataset
data = Dataset.load_builtin('ml-100k')

# Define a reader to parse the data
reader = Reader(line_format='user item rating timestamp', sep='\t', rating_scale=(1, 5))
# Load the data
data = Dataset.load_from_file('data/interim/ml-100k/u.data', reader)
# cross_validate_algo = pickle.load(open('../models/knnpickle_file', 'rb'))

# Split the data into 5 folds for cross-validation
cross_validate_algo = KNNBasic(sim_options={'user_based': False})
cross_validate_results = cross_validate(cross_validate_algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Print the cross-validation results
print("Mean RMSE:", sum(cross_validate_results['test_rmse']) / 5)
print("Mean MAE:", sum(cross_validate_results['test_mae']) / 5)
