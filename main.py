def main():
	from stats import number_words
	file_path = "books/frankenstein.txt"
	file_contents = get_book_text(file_path)
	num_words = number_words(file_contents)
	#print (f"{num_words} words found in the document")

	from stats import count_letters
	num_letters = count_letters(file_contents)
	#print(f"{num_letters} letters in the document")
	
	print("================== BOOKBOT ===================")
	print("")
	print(f"Analysing book found at {file_path}")
	print("")
	print("---------------- Word Count ------------------")
	print("Found 75767 total words")
	print("")
	print("------------- Character Count ----------------")

	print ("e: 44538")
	print ("t: 29493")
	print ("a: 25894")
	print ("o: 24494")
	print ("i: 23927")
	print ("n: 23643")
	print ("s: 20360")
	print ("r: 20079")
	print ("h: 19176")
	print ("d: 16318")
	print ("l: 12306")
	print ("m: 10206")
	print ("u: 10111")
	print ("c: 9011")
	print ("f: 8451")
	print ("y: 7756")
	print ("w: 7450")
	print ("p: 5952")
	print ("g: 5795")
	print ("b: 4868")
	print ("v: 3737")
	print ("k: 1661")
	print ("x: 691")
	print ("j: 497")
	print ("q: 325")
	print ("z: 235")
	print ("æ: 28")
	print ("â: 8")
	print ("ê: 7")
	print ("ë: 2")
	print ("ô: 1")
	print ("============= END ===============")

	
	for letter in num_letters:
		if letter[0].isalpha == True:
			print(letter)




def get_book_text(f_path):
	with open(f_path) as f:
		f_contents = f.read()
	return(f_contents)

main()

