import pandas as pd
import numpy as np
import string

# import data
df1 = pd.read_csv('Raw_data\S08_question_answer_pairs.txt', sep='\t',encoding = 'ISO-8859-1')
df2 = pd.read_csv('Raw_data\S09_question_answer_pairs.txt', sep='\t',encoding = 'ISO-8859-1')
df3 = pd.read_csv('Raw_data\S10_question_answer_pairs.txt', sep='\t',encoding = 'ISO-8859-1')

df2.tail()

# combine dataframe
df = df1.append([df2, df3])
df=df.reset_index(drop=True)
df.info()
df.tail()

# remove punctuations in Question and answer
df["Question"] = df['Question'].str.replace(r'[^\w\s]+', '')
df["Answer"] = df['Answer'].str.replace(r'[^\w\s]+', '')

#change question and answer to lower letter
df['Question']=df['Question'].str.lower()
df['Answer']=df['Answer'].str.lower()

# drop duplicates
df = df.drop_duplicates()
df.shape

# repalce entire space in a cell by null
df = df.apply(lambda x: x.str.strip()).replace('', np.nan)

# drop null of question and answer
df = df.dropna(subset=['Question','Answer'])
df=df.reset_index(drop=True)
df.shape

df=df.sample(frac=1).reset_index(drop=True)
df.tail(10)

#split training, validation, test set by 0.7, 0.15, 0.15
n1=round(len(df)*0.7)
n2=round(len(df)*0.15)
train_df=df.iloc[0:n1,:].reset_index(drop=True)
vail_df=df.iloc[n1:n1+n2,:].reset_index(drop=True)
test_df=df.iloc[n1+n2:,:].reset_index(drop=True)

train_df.shape

# export cleaned dataset
train_df.to_csv(r"Dataset\train_df.csv",encoding="utf-8")
vail_df.to_csv(r"Dataset\vail_df.csv",encoding="utf-8")
test_df.to_csv(r"Dataset\test_df.csv",encoding="utf-8")