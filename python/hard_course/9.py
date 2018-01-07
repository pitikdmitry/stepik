import requests
import re


def check_content(res: object) -> str:
    text = res.text
    print(text)
    template = r"<a href=[\w./:]+>"
    match_object = re.match(template, text)
    print(match_object)


# url_1 = input()
# url_2 = input()
url_1 = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
url_2 = "https://stepic.org/media/attachments/lesson/24472/sample2.html"

res = requests.get(url_1)
print(res.status_code)
check_content(res)


