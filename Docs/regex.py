import re


def extract_word(text):
    print("Input Text::{}".format(text))
    regex = r"(\w|\s)*"
    matches = re.finditer(regex, text, re.DOTALL)
    newstr = ''
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        newstr = newstr + match.group()
    print("Output Text::{}".format(newstr))
    return newstr
