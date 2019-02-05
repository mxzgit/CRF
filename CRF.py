## Source : https://towardsdatascience.com/conditional-random-field-tutorial-in-pytorch-ca0d04499463
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import codecs
import nltk 
from sklearn.model_selection import train_test_split
import pycrfsuite
import numpy as np
from sklearn.metrics import classification_report



with codecs.open("reuters.xml","r","utf-8") as f:
	soup = bs(f,"html5lib")


docs = []
for element in soup.find_all("document"):
	# print(element)

	texts = []

	for c in element.find("textwithnamedentities").children:
		if type(c) == Tag :
			if c.name == "namedentityintext":
				label = "N"

			else : 
				label = "I"

			for w in c.text.split(" "):
				if len(w) > 0:
					texts.append((w,label))  

	docs.append(texts)

data = []
for i, doc in enumerate(docs):
	tokens = [t for t,label in doc]

	tagged = nltk.pos_tag(tokens)

	data.append([(w,pos,label) for (w,label),(word,pos) in zip(doc,tagged)])



def word2feature(doc,i):
	word = doc[i][0]
	postag = doc[i][1]



	feature = [
		'bias',
		'word.lower='+word.lower(),
		'word[-3]='+word[-3:],
		'word[-2]='+word[-2:],
		'word.isupper=%s'%word.isupper(),
		'word.istitle=%s'%word.istitle(),
		'word.isdigit=%s'%word.isdigit(),
		'postag='+postag

		]

	if i > 0:
		word1 = doc[i-1][0]
		postag1 = doc[i-1][1]
		feature.extend([
			'-1:word.lower='+word.lower(),
			'-1:word.isupper=%s'%word.isupper(),
			'-1:word.istitle=%s'%word.istitle(),
			'-1:word.isdigit=%s'%word.isdigit(),
			'-1:postag='+postag
			])
	else :
		feature.append('BOS')
	
	if i < len(doc)-1:
		word1 = doc[i+1][0]
		postag1 = doc[i+1][1]
		feature.extend([
			'+1:word.lower='+word.lower(),
			'+1:word.isupper=%s'%word.isupper(),
			'+1:word.istitle=%s'%word.istitle(),
			'+1:word.isdigit=%s'%word.isdigit(),
			'+1:postag='+postag
			])
	else :
		feature.append('EOS')

	return feature

def extract_feature(doc):
	return [word2feature(doc,i) for i in range(len(doc))]


def get_labels(doc):
	return [label for (token,postag,label) in doc]

x = [extract_feature(doc) for doc in data]
y = [get_labels(doc) for doc in data]

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2)

"""
trainer = pycrfsuite.Trainer(verbose=True)
for xseq, yseq in zip(X_train,Y_train):
	trainer.append(xseq,yseq)

trainer.set_params({
	'c1':0.1,
	'c2':0.01,
	'max_iterations':200,
	'feature.possible_transitions':True
	})

trainer.train('crf.model')
"""

tagger = pycrfsuite.Tagger()
tagger.open('crf.model')
Y_pred = [tagger.tag(xseq) for xseq in X_test]

i = 12

for x,y in zip(Y_pred[i], [x[1].split("=")[1] for x in X_test[i]]):
	print("%s (%s)"%(y,x))


labels = {"N":1,"I":0}

predictionq = np.array([labels[tag] for row in Y_pred for tag in row])
truth       = np.array([labels[tag] for row in Y_test for tag in row])

print(classification_report(
	truth,predictionq,
	target_names=["I","N"])) 
