# s  = sentence.index('is fun')
# e  = sentence.rindex('is fun')
# Is = sentence[:s].count(" ")
# Ie = sentence[s:e].count(" ") + Is


sentence = "mehdi is a mehdi"
searching = 'mehdi'
s  = sentence.index(searching)
e  = sentence.rindex(searching)
Is = sentence[:s].count(" ")
Ie = searching.count(" ") + Is






def pos_calc(sentence,search_str):
	#print(len(sentence),len(search_str))

	data  = []
	start = 0
	end   = len(sentence)
	truth = True


	Is = 0
	Ie = 0
	
	while (truth):
		truth = False

		s  = 0 

		if (search_str in sentence[start:end]):

			truth = True
			s = sentence[start:end].index(search_str)
			print('"{}"'.format(sentence[start:s+1]))
			print(sentence[start:s].count(" "))
			#Is = sentence[start:s].count(" ")+Ie
			#print(" " in sentence[start-1:s])
			#Ie += search_str.count(" ") + Is
			#data.append((Is,Ie,"out_coll"))
			start += len(search_str)
			#print(start,s)

	return data



print(pos_calc("mehdi mehdi","mehdi"))