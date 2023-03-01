import re
import utils
with open('tsis5/regex/parsing/row.txt', 'r', encoding='utf-8') as f:
    text = f.read()
pattern_body = r'Фискальный признак:(.*)WEBKASSA.KZ'
matching_body = re.search(pattern_body, text, re.DOTALL)
if matching_body is not None:
    print(matching_body.group())


