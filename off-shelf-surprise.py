import pandas as pd
import numpy as np

from surprise import SVD
from surprise import NormalPredictor
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate

uid, mid, rating = np.loadtxt('./data/data.txt', delimiter='\t', usecols = (0,1,2), unpack = True)

ratings_dict = {'itemID': uid,
                'userID': mid,
                'rating': rating}

df = pd.DataFrame(ratings_dict)

reader = Reader(rating_scale=(1, 5))

# load data
data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)

algo = SVD()

cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)
