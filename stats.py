def number_words(full_text):
	split_text = full_text.split(' ')
	return len(split_text)

def count_letters(full_text):
	freq = {}
	count = 0
	test = {}


	for letter in full_text:
		letter = letter.lower()
		if letter in freq:
			freq[letter] +=1 
		else:
			freq[letter] = 1
	
	#print(freq["t"])
	
	characters_sorted = sorted(freq.items(), reverse = True, key = lambda item : item[1])
	
	#print(characters_sorted)


##	test['t'] = 29493
##	test['p'] = 5952
##	test['c'] = 9011	
		
	return(characters_sorted)




