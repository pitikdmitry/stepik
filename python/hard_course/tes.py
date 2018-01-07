import re

text = "<a href=https://stepic.org/media/attachments/lesson/24472/sample1.html>1</a>"
template = r"<a href=.+>"
match_object = re.findall(template, text)
print(match_object)