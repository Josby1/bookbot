def main():
	file_path = "books/frankenstein.txt"
	file_contents = get_book_text(file_path)
	num_words = number_words(file_contents)
	print (f"{num_words} words found in the document")
	
	
	


def get_book_text(f_path):
	with open(f_path) as f:
		f_contents = f.read()
	return(f_contents)

def number_words(full_text):
	split_text = full_text.split(' ')
	return len(split_text)


	


main()

