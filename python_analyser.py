import copy
import string
import re


def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())


def is_not_empty_line(line):
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    line = line.replace('\t', '')
    line = line.replace('\r', '')
    return len(line) != 0


def count_not_empty_lines(filename):
    counter = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            if is_not_empty_line(line):
                counter += 1
    return counter


def count_comment_lines(filename):
    # this function returns number of comment lines
    # don't forget that comment starts with hash "#"
    counter = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            line_without_white_sign = copy.copy(line)
            line_without_white_sign = line_without_white_sign.replace(" ", "")
            line_without_white_sign = line_without_white_sign.replace("\t", "")
            if line_without_white_sign[0] == '#':
                counter += 1
    return counter


def count_code_lines(filename):
    # this function returns number of code lines
    counter = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            temp_line = copy.copy(line)
            temp_line = temp_line.replace(" ", "")
            temp_line = temp_line.replace("\t", "")
            if temp_line[0] != '#' and is_not_empty_line(temp_line):
                counter += 1
    return counter


def remove_no_words(words):
    result = []
    for word in words:
        if word != "" and word != "\n" and word != ":" and word != ";" and word != "+" \
                and word != "-" and word != "*" and word != "/" and word != "#" and word != ":\n" \
                and not re.match(r"^[-]*$", word) and word != '==' and word != '!=' and word != '+=' \
                and word != '-=' and word != '/=' and word != '*=' and word != '%':
            result.append(word)
    return result


def split_connected_words(words):
    result = []
    for word in words:
        if "(" in word:
            result.extend(word.split("("))
        elif ")" in word:
            result.extend(word.split(")"))
        elif "[" in word:
            result.extend(word.split("["))
        elif "]" in word:
            result.extend(word.split("]"))
        elif "{" in word:
            result.extend(word.split("{"))
        elif "}" in word:
            result.extend(word.split("}"))
        elif "." in word:
            result.extend(word.split("."))
        elif ":" in word:
            result.extend(word.split(":"))
        else:
            result.append(word)
    return result


def count_words(filename):
    # this function returns number of words in file (#,:,etc, ==, +, etc) are not words
    counter = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            temp_line = line.split(" ")

            words = remove_no_words(temp_line)
            words = split_connected_words(words)
            words = remove_no_words(words)

            for word in words:
                counter += 1
    return counter


def count_word(filename, word):
    # this function returns number of occurence of word in the file
    counter = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            counter += len(re.findall(word, line))
    return counter


def count_comment_words(filename):
    # this function returns number of words in all comments
    counter = 0
    with open(filename) as file:
        for line in file.readlines():
            if re.match(r"^[ ]*#", line) or line[0] == "#":
                words = line.split(" ")
                for word in words:
                    if word != '' and word != '#':
                        counter += 1
    return counter


def count_syntax(filename, syntax_word):
    # this function should handle following syntax words: if, else, elif, for, while, return, class, def, try, except
    # remember that "if" can occure in comments and commented lines of code f.e #while True: 
    # should not be counted. This function should return the number of syntax_word occurence in the file.
    counter = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            if not re.match(r"^[ ]*#", line) or line[0] != "#":
                counter += len(re.findall(syntax_word, line))
    return counter
