import pandas as pd

data = pd.read_json('data_kelkoo.json',lines=True)

#print(data.head(5))
print(data.columns)

classes = ['brand', 'no_class']


for i in range(data.shape[0]):
	print(data[classes[0]].iloc[i])


# s  = sentence.index('is fun')
# e  = sentence.rindex('is fun')
# Is = sentence[:s].count(" ")
# Ie = sentence[s:e].count(" ") + Is