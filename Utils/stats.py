import pandas as pd

def info(data):
    
    maxx = []
    minn = []
    for i in data.columns:
        maxx.append(data[i].value_counts().max())
        minn.append(data[i].value_counts().min())
        
    df = pd.DataFrame(
        {'dtype': data.dtypes,
         'len': len(data),
         'duplication': len(data) - data.nunique(),
         'nunique': data.nunique(),
         'null': data.isnull().sum(),
         'null_percent': data.isnull().sum() / len(data)},
        columns = ['dtype', 'len', 'nunique', 'duplication', 'null', 'null_percent']
    )
    
    return df