import numpy as np

# Calculate the position of tags

def pos_calc(sentence,search_str,tag):
	
	sentence = sentence.lstrip()
	search_str = search_str.lstrip()

	data  = []
	start = 0
	end   = len(sentence)
	truth = True


	Is = 0
	Ie = 0
	s  = 0 
	#tag = search_str.replace(" ","_")
	while (truth):
		truth = False

		if (search_str in sentence[start:end]):

			truth = True
			s = sentence[start:end].index(search_str)
			Is = sentence[start:start+s].count(" ")+Ie
			Ie = search_str.count(" ") + Is
			data.append((Is,Ie,search_str,tag))
			start += len(search_str) + len(sentence[start:start+s])
			
	return data

# Tags every elment in the string
def pos_tag(sentence,data):

	sentence = sentence.lstrip()
	sentence = sentence.split(" ")

	tags = ["O"]*len(sentence)

	for element in data:
		tags[element[0]] = "B-"+element[3]

		if (element[0] != element[1]):
			tags[element[1]] = "E-"+element[3]
			for i in range(element[0]+1,element[1]):
				tags[i] = "I-"+element[3]
	
	return tags

def list_tags(sentence,tags,tag):

	sentence = sentence.lstrip()

	final_tags = []
	list_tags = []
	
	for element in tags:
		data = pos_calc(sentence,element,tag)
		list_tags.append(pos_tag(sentence,data))

	list_tags = np.array(list_tags)
	


	for i in range(len(list_tags[0])):

		sub_set = set(list_tags[0:,i])
		if(len(sub_set) == 1 and "O" in sub_set):
			final_tags.append("O")
		elif(len(sub_set) == 1 and "O" not in sub_set):
			final_tags.append(list(sub_set)[0])
		else: 
			sub_set.remove("O")
			final_tags.append(list(sub_set)[0]) 


	return final_tags

def tag_sentences(sentence,dic_tags):

	return [list_tags(sentence,dic_tags[tag],tag) for tag in dic_tags]



def clean_tags(lists):
	
	final_result = []


	for i in range(len(lists)):
		sub_list = np.array(lists[i])
		final_tags = []

		for j in range(len(sub_list[0])):
			sub_set = set(sub_list[0:,j])
			if(len(sub_set) == 1 and "O" in sub_set):
				final_tags.append("O")
			elif(len(sub_set) == 1 and "O" not in sub_set):
				final_tags.append(list(sub_set)[0])
			else: 
				sub_set.remove("O")
				final_tags.append(list(sub_set)[0]) 

		final_result.append(final_tags)

	return final_result



if __name__=="__main__":

	results = []

	sentences = ["outdoor collection ballerines toile corail blanc 40",
	"outdoor collection blouse rayee col tunisien gris 44",
	"outdoor collection chemise maille imprimee ecru gris 42 44",
	"outdoor collection jean battle coupe droite stone 48",
	"outifrance sangle d arrimage a crochets pro",
	"ouvre boites manche rond",
	"ovation pneu ovation w 586 xl 225 40r18 92 h tourisme hiver",
	"overseas oreiller 40x60cm coton gris"]

	tags = ["outdoor collection", "maille", "outifrance","pro","ovation","overseas","gris"]

	dic_tags = {"brand":["outdoor collection", "maille", "outifrance","pro","ovation","overseas"],
				"details":["40"],
				"couleur":["blanc","corail","gris","ecru"],
				}
				
	for sentence in sentences:
		results.append(tag_sentences(sentence,dic_tags))
	

	results = clean_tags(results)

	print(results)