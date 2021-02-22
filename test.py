import pandas as pd
data

def load_csv(filename):
    data=pd.read_csv(filename)
    print(data.head(5),data.shape)
    return data

def clean_data():
    data = load_csv("netflix_titles.csv")
    new_data= data.dropna()
    return new_data

Data