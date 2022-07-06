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
    def __init__():
        pass

    def getDTR(self, params):
        #criterion, max_depth, max_features
        #min_samples_leaf, random_state
        return DecisionTreeRegressor()


    def getRFR(self, params):
        #n_estimators, criterion, max_depth, max_features
        #min_samples_leaf, random_state
        return RandomForestRegressor()