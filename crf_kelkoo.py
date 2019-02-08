import pandas as pd
import tags as tg
import numpy as np
import time
from collections.abc import Iterable
from multiprocessing import Pool


st = time.time()


num_partitions = 1000
num_cores = 4
#data = pd.read_json('offers_tagged_20k.json',lines=True)

result = pd.read_csv('mehdi.csv',sep=',')
dic_tags_new = {}
list_tags = ["brand","colour","details","material","object"]
#data["result"] = ["0"]*data.shape[0]

'''
for tag in list_tags:

	dic_tags_new[tag] = []

	if (all(x == None for x in data[tag].values)):
		continue
	else:
		for value in data[tag].values:
			if (isinstance(value, Iterable)):
				for sub_value in value:
					dic_tags_new[tag].append(sub_value)

			dic_tags_new[tag] = list(set(dic_tags_new[tag]))

results = []

def func_tag(data):
	data["result"] = data["titleNormalized"].apply(lambda x:tg.tag_sentences(x,dic_tags_new))
	return data

result = parallelize_dataframe(data,func_tag)
'''
def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


"""
data.result = data.titleNormalized.apply(lambda x:tg.tag_sentences(x,dic_tags_new))
data.result = data.result.apply(lambda x:tg.clean_tags(x))
"""



def func_clean(data):
	data["result"] = data["result"].apply(lambda x:tg.clean_tags(x))
	return data


result_me = parallelize_dataframe(result,func_clean)
print(data.titleNormalized.iloc[0])
print(data.result.iloc[0])

result_me.to_csv('mehdi.csv',sep=',')
print(time.time() - st)
