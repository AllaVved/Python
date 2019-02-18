"""
1. Получить common words со страниц, на которые есть ссылки

    Получить ссылки на соседние страницы.
    Спарсить отдельно соседние страницы.
    Сложить все в один список.

"""
import re
import requests

topic = "баран"

link = f"https://ru.wikipedia.org/wiki/{topic.capitalize()}"
html_content = requests.get(link).text
words_a = re.findall("<a href=\"/wiki/(.+)\" title=\".+\">[а-яА-Я\-\' ()]{3,}</a>", html_content)
list_all = []
i = 0
while i < len(words_a):
    link_a = f"https://ru.wikipedia.org/wiki/{words_a[i]}"
    html_content = requests.get(link_a).text
    words = re.findall("[а-яА-Я\-\']{3,}", html_content)
    list_all.extend(words)
    i += 1
    print(i) # Просто чтобы видеть что что-то происходит
rate = {}
for word in list_all:
    if word in rate:
        rate[word] += 1
    else:
        rate[word] = 1
rate_list = list(rate.items())
rate_list.sort(key=lambda x: -x[1])
print(rate_list[0:30])
