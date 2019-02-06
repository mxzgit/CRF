def pos_calc(sentence,search_str):

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
			data.append((Is,Ie,"out_coll"))
			start += len(search_str) + len(sentence[start:start+s])
			
	return data



print(pos_calc("mehdi is a mehdi lsks,lsjdkls zidpzoz mehdi ,azdjad mehdi","mehdi is"))