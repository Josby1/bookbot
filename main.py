def main():
	import sys

	try:
		file_path = f"{sys.argv[1]}"
	except IndexError:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)


#	if len(sys.argv) <=1 :
#		print("Usage: python3 main.py <path_to_book>")
#		exit()
	



	from stats import number_words


	file_contents = get_book_text(file_path)
	num_words = number_words(file_contents)
	#print (f"{num_words} words found in the document")

	from stats import count_letters
	num_letters = count_letters(file_contents)
	#print(f"{num_letters} letters in the document")
#	print("================== BOOKBOT ===================")
#	print("")
#	print(f"Analysing book found at {file_path}")
#	print("")
#	print("---------------- Word Count ------------------")
#	print("")
#	print(f"Found {num_words} total words")
#	print("")
#	print("------------- Character Count ----------------")

	for letter in num_letters:
		if letter[0] == 'e' :
			print (f"{letter[0]}: {letter[1]}")
		if letter[0] == 't' :
			print (f"{letter[0]}: {letter[1]}")
		

#	print ("============= END ===============")

	
def get_book_text(f_path):
	with open(f_path) as f:
		f_contents = f.read()
	return(f_contents)

main()

