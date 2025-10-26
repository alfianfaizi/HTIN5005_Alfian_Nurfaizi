# -*- coding: utf-8 -*-
"""
#HTIN5005 Assignment 2 - Alfian Nurfaizi (550180999)
#SCI-XAI Pipeline adapted from https://github.com/petmoreno/SCI-XAI-Pipeline.git
"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

#Count values of every feature of the df
def df_values(df):
    for i in range(0, len(df.columns)):
        print("*****start of feature ", df.columns[i], "*************************")
        print (df.iloc[:,i].value_counts())       
        print ("*****end of feature ", df.columns[i], "************************** \n")

#Print info() method with an extra column of % of non-null values
def info_adhoc(df):
    d=(df.count()/len(df))*100
    df_info=pd.DataFrame(data=d, columns=['% non-null values'])
    df_info['non-null values']=df.count()
    df_info['dtype']=df.dtypes
    return df_info

#Convert category attributes to their num codes
def cat_to_codes(df, cat_feat):
    df_cat_coded=df
    for i in range(len(cat_feat)):
            df_cat_coded.loc[:,cat_feat[i]]=df_cat_coded.loc[:,cat_feat[i]].cat.codes    
    #The NaN has been coded to -1. So we have to revert it for the imputer
    df_cat_coded.replace(to_replace=-1,value=np.NAN,inplace=True)
    return df_cat_coded

