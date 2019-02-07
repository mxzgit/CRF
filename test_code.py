def pos_calc(sentence,search_str):
	

	sentence = sentence.lstrip()
	search_str = search_str.lstrip()

	data  = []
	start = 0
	end   = len(sentence)
	truth = True


	Is = 0
	Ie = 0
	s  = 0 

	while (truth):
		truth = False

		if (search_str in sentence[start:end]):

			truth = True
			s = sentence[start:end].index(search_str)
			Is = sentence[start:start+s].count(" ")+Ie
			Ie = search_str.count(" ") + Is
			data.append((Is,Ie,search_str,"out_coll"))
			start += len(search_str) + len(sentence[start:start+s])
			
	return data


def pos_tag(sentence,data):

	sentence = sentence.lstrip()
	sentence = sentence.split(" ")
	

	final_data = []
	tags = ["O"]*len(sentence)

	for element in data:
		tags[element[0]] = "B-"+element[3]
	
	final_data.append(tags)
	return final_data

data = pos_calc("mehdi is a mehdi","mehdi")
print(pos_tag("mehdi is a mehdi",data))