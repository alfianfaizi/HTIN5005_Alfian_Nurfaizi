# -*- coding: utf-8 -*-
"""
#HTIN5005 Assignment 2 - Alfian Nurfaizi (550180999)
#SCI-XAI Pipeline adapted from https://github.com/petmoreno/SCI-XAI-Pipeline.git
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:44:17 2020
@author: k5000751

This file has been updated to fix type conflicts and avoid SettingWithCopyWarning.
"""
#This class must include as much as function needed depeding on the
#mispelling or wrong character detected in the dataset
import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

#Class for correcting misspelling of features and target columns
class ageRounder(BaseEstimator, TransformerMixin):
    def rounder (self,df):
    #Some fetures content seems to have the character \t.
    #Let's remove such character for the sake of consistency
        #print('\n>>>>>>>>Calling rounder')
        df_out = df.copy()
        df_out['age']=np.around(df_out['age'])
        return df_out

    def __init__(self):
        print('\n>>>>>>>>Calling init() from ageRounder')

    def fit(self, X, y=None):
        print('\n>>>>>>>>Calling fit() from ageRounder')
        return self

    def transform(self,X,y=None):
        print('\n>>>>>>>>Calling transform() from ageRounder')
        df=self.rounder(X)
        return df

    def fit_transform(self, X, y=None,):
        return self.fit(X, y).transform(X, y)

#**************************************************************
#************Below it is inherited from CKD predictor
#**************************************************************
def misspellingCorrector(df):
    df.iloc[:] = df.iloc[:].str.replace(r'\t','')
    df.iloc[:] = df.iloc[:].str.replace(r' ','')
    return df


#Class for correcting misspelling of features and target columns
class misspellingTransformer_old(BaseEstimator, TransformerMixin):
    def misspelling (self,df):
    #Some fetures content seems to have the character \t.
    #Let's remove such character for the sake of consistency
        for i in range(0, len(df.columns)):
            if df.dtypes[i]==np.object:
                df.iloc[:,i] = df.iloc[:,i].str.replace(r'\t','')
                df.iloc[:,i] = df.iloc[:,i].str.replace(r' ','')
        return df

    def __init__(self,target_name):
        print('\n>>>>>>>>Calling init() from misspelling')
        self.target_name=target_name

    def fit(self, X, y=None):
        print('\n>>>>>>>>Calling fit() from misspelling')
        return self

    def transform(self,X,y=None):
        print('\n>>>>>>>>Calling transform() from misspelling')
        df=pd.concat([X,y],axis=1)
        df=self.misspelling(df)
        y=df.loc[:,self.target_name]
        X=df.drop(self.target_name,axis=1)
        return X,y
    def fit_transform(self, X, y=None,):
        return self.fit(X, y).transform(X, y)

#Class for correcting misspelling of features and target columns
class misspellingTransformer(BaseEstimator, TransformerMixin):
    def misspelling (self,df):
    #Some fetures content seems to have the character \t.
    #Let's remove such character for the sake of consistency
        print('\n>>>>>>>>Calling misspelling')
        df_out = df.copy()
        for col in df_out.columns:
            if df_out[col].dtype == 'object' or pd.api.types.is_categorical_dtype(df_out[col]):
                df_out[col] = df_out[col].astype(str).str.replace(r'\t','', regex=True)
                df_out[col] = df_out[col].astype(str).str.replace(r' ','', regex=True)
        return df_out

    def __init__(self):
        print('\n>>>>>>>>Calling init() from misspelling')

    def fit(self, X, y=None):
        print('\n>>>>>>>>Calling fit() from misspelling')
        return self

    def transform(self,X,y=None):
        print('\n>>>>>>>>Calling transform() from misspelling')
        df=self.misspelling(X)
        return df

    def fit_transform(self, X, y=None,):
        return self.fit(X, y).transform(X, y)

#Class for downcasting last category value of features 'al' and 'sg'
class CastDown(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>>Calling init() from CastDown')

    def fit(self,X, y=None):
        print('\n>>>>>>>>Calling fit() from CastDown')
        return self

    def transform(self, X, y=None):
        print('\n>>>>>>>>Calling transform() from CastDown')
        X_out = X.copy() # Avoid SettingWithCopyWarning
        for col in X_out.columns:
            # Replace both integer 5 and string '5'
            X_out[col] = X_out[col].replace(5, 4)
            X_out[col] = X_out[col].replace('5', '4')
        return X_out


#Class to be included in TransfromColumn pipeline for casting numeric columns to float64
class Numeric_Cast_Column(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>>Calling init() from Numeric_Cast_Column')
    def fit(self, X,y=None):
        #print('inside fit Numeric_Cast, tuple leng', len(X))
        print('\n>>>>>>>>Calling fit() from Numeric_Cast_Column')
        return self

    def transform(self, X,y=None):
        #print ('Content of X', X)
        print('\n>>>>>>>>Calling transform() from Numeric_Cast_Column')
        X_out = X.copy()
        for col in X_out.columns:
            X_out[col]=pd.to_numeric(X_out[col],errors='coerce')
        return X_out

    def fit_transform(self, X,y=None):
        return self.fit(X, y).transform(X, y)


#Class to be included in TransfromColumn pipeline for casting numeric columns to float64
class Category_Cast_Column(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>>Calling init() from Category_Cast_Column')
    def fit(self, X,y=None):
        #print('inside fit Numeric_Cast, tuple leng', len(X))
        print('\n>>>>>>>>Calling fit() from Category_Cast_Column')
        return self

    def transform(self, X,y=None):
        #print ('Content of X', X)
        print('\n>>>>>>>>Calling transform() from Category_Cast_Column')
        X_out = X.copy()
        for col in X_out.columns:
            # FIX: Convert all to string FIRST to ensure uniform type
            X_out[col]=X_out[col].astype(str)
            X_out[col]=X_out[col].astype('category')
        return X_out

    def fit_transform(self, X,y=None):
        return self.fit(X, y).transform(X, y)

# This is a duplicate class, removing the second definition
# class ageRounder(BaseEstimator, TransformerMixin):
#     def rounder (self,df):
#     #Some fetures content seems to have the character \t.
#     #Let's remove such character for the sake of consistency
#         print('\n>>>>>>>>Calling rounder')
#         df['age']=np.around(df.loc[:,'age'])
#         return df

#     def __init__(self):
#         print('\n>>>>>>>>Calling init() from ageRounder')

#     def fit(self, X, y=None):
#         print('\n>>>>>>>>Calling fit() from ageRounder')
#         return self

#     def transform(self,X,y=None):
#         print('\n>>>>>>>>Calling transform() from ageRounder')
#         df=self.rounder(X)
#         return df

#     def fit_transform(self, X, y=None,):
#         return self.fit(X, y).transform(X, y)