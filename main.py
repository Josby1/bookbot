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
	print("")
	print(f"Found {num_words} total words")
	print("")
	print("------------- Character Count ----------------")

	for letter in num_letters:
		if letter[0].isalpha():
			print (f"{letter[0]} : {letter[1]}")
		

	print ("============= END ===============")

	
			




def get_book_text(f_path):
	with open(f_path) as f:
		f_contents = f.read()
	return(f_contents)

main()

