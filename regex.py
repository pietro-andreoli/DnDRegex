
import re

# \. Start selection with the period character
# [^.]* Look for 0 or more characters that arent the period character
# \d{1,2} Look for 1 or 2 numbers in a row
full_sentence_arg = "\.[^.]*at \d{1,2}th level[^.]*\."

open_beginning_sentence_arg = "[A-Z][^.]*at \d{1,2}th level[^.]*\."


def get_file_contents(file_name):
	file_contents = ""
	with open(file_name) as file:
		file_contents = file.read()
	return file_contents


def get_sentences(file_name):
	file_contents = get_file_contents(file_name)
	surrounding_periods_re = re.compile(full_sentence_arg, re.IGNORECASE)
	re_occurrences = surrounding_periods_re.findall(file_contents)
	# print(str(re_occurrences))

	open_beginning_sentence_re = re.compile(open_beginning_sentence_arg)
	re_occurrences = re_occurrences + open_beginning_sentence_re.findall(file_contents)
	output_file = "results_" + file_name
	# fill_file(output_file, str(re_occurrences), 'w')
	return re_occurrences, output_file


def strip_file(file_name):
	file_contents = get_file_contents(file_name)
	expression_tags = "<(?!br[^>]*>|\/{0,1}h[0-9]+[^>]*>)[^>]*>"
	expression_curly = "{.*}"
	compiled_expression = re.compile(expression_tags)
	new_str = re.sub(compiled_expression, '', file_contents)
	compiled_expression = re.compile(expression_curly)
	new_str = re.sub(compiled_expression, '', new_str)
	new_file_name = "stripped_" + file_name
	fill_file(new_file_name, new_str, 'w')
	return new_file_name


def fill_file(file_name, data, file_modifier):
	with open(file_name, file_modifier) as file:
		file.write(data)
