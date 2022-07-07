import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import lightgbm as lgbm
import xgboost as xgb

from Meals import Meals
#lgbm.LGBMRegressor(boosting_type=)

params = {}
DTR_param ={
    
}
class MakeReg:
    def __init__(self):
        pass

    def getDTR(self, params):
        #max_depth, max_features
        #min_samples_leaf, random_state
        return DecisionTreeRegressor(
            max_depth=params['max_depth'],
            max_features=params['max_features'],
            min_samples_leaf = params['min_samples_leaf'],
            random_state=params['random_state'],
        )


    def getRFR(self, params):
        #n_estimators, criterion, max_depth, max_features
        #min_samples_leaf, random_state
        return RandomForestRegressor(
            max_depth=params['max_depth'],
            max_features=params['max_features'],
            min_samples_leaf = params['min_samples_leaf'],
            random_state=params['random_state'],
            n_estimators=params['n_estimators'],
        )

params = {'min_samples_leaf' : 3,
    'max_depth' : 2,
    'max_features': 0.7,
    'random_state' : 42,
}


print(MakeReg().getDTR(params))