'''
This is an implementation of Ensemble Partial Least Squares Regression
'''

import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.ensemble import BaggingRegressor

class EPLSRegression(object):
    
    '''
    def __init__(self)
                 #, n_estimators = 10, max_samples = 1.0, max_features = 1.0,
                 #bootstrap = True, bootstrap_features = False, oob_score = False, 
                 #random_state = None, verbose = 0)#, n_components = 2, scale = True, max_iter = 500, copy = True)
    
        pls = PLSRegression(n_componenets = n_components, scale = scale, max_iter = max_iter, 
                            tol = tol, copy = copy)
        self.enpls = BaggingRegressor(base_estimator = pls, n_estimators = n_estimators, max_samples = max_samples,
                                 max_features = max_features, bootstrap = bootstrap, bootstrap_features = bootstrap_features,
                                 oob_score = oob_score, warm_start = warm_start, n_jobs = n_jobs, random_state = random_state,
                                 verbose = verbose)
        return self
        
    def fit(self, X, y): 
        self.enpls.fit(X, y)
        return self 
        
    def predict(self, X): 
        return self.enpls.predict(X) 
    '''
    def __init__(self, n_estimators, max_samples)
                 #bootstrap = True, bootstrap_features = False, oob_score = False, 
                 #random_state = None, verbose = 0)#, n_components = 2, scale = True, max_iter = 500, copy = True)
            
                    