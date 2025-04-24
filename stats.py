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

	test['t'] = 29493
	test['p'] = 5952
	test['c'] = 9011	
		
	return(letter,freq, test)
