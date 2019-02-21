import pandas as pd

def extract_tags(df,tags):
    
    result = pd.DataFrame()
    for tag in tags:
        result[tag] = df[tag].unique()
    return result



