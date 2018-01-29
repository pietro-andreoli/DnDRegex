import re

#\. Start selection with the period character
#[^.]* Look for 0 or more characters that arent the period character
#\d{1,2} Look for 1 or 2 numbers in a row
full_sentence_arg = "\.[^.]*at \d{1,2}th level[^.]*\."

open_beginning_sentence_arg = "[A-Z][^.]*at \d{1,2}th level[^.]*\."

def strip_file(file_name):
	file_contents = ""
	with open(file_name + ".html") as file:
		file_contents = file.read()
	surrounding_periods_re = re.compile(full_sentence_arg, re.IGNORECASE)
	re_occurrences = surrounding_periods_re.findall(file_contents)
	#print(str(re_occurrences))

	open_beginning_sentence_re = re.compile(open_beginning_sentence_arg)
	re_occurrences_new = open_beginning_sentence_re.findall(file_contents)
	print(re_occurrences_new)
	print("test2")
