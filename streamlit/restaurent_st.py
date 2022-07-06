import pandas as pd
import numpy as np
import streamlit as st
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from time import time

import Regressor
import Meals

regressor = Regressor.MakeReg()


with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        st.success("Done!")

st.title('한국토지주택공사 식수 인원 예측')
models = ('DecisionTreeRegressor',
         'RandomForestRegressor',
         'GradientBoostingRegressor',
         'lightGBM',
         'XGBoost')
option = st.selectbox(
    '원하는 모델을 골라주세요.',
    models
)
#n_estimators, criterion, max_depth, max_features
#min_samples_leaf, random_state
DTR_h_params = {
            'max_depth' : [10, 50],
            'max_features' : [0.0, 1.0],
            'min_samples_leaf': [1, 10],
            'random_state' : [1, 100],
}
RFR_h_params = DTR_h_params.copy()
RFR_h_params['n_estimators'] = [100, 500]

params = {}
if option == 'DecisionTreeRegressor':
    params.clear()
    for key, value in DTR_h_params.items():
        params[key] = st.slider(key, 
        value[0], value[1], value[0])
    
    model = 
    
elif option =='RandomForestRegressor':
    params.clear()
    for key, value in RFR_h_params.items():
        params[key] = st.slider(key, 
        value[0], value[1], value[0])

for key, value in params.items():
    st.write(key, value)

st.write(option)


st.markdown('Streamlit is **_really_ cool**.')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))




