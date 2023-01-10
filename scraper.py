import requests
from parser_1 import parse


if __name__ == '__main__':
    url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
    response = requests.get(url)
    results = parse(response.text)
    print(results)

# import requests
# from bs4 import BeautifulSoup


# url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
# r = requests.get(url)
# markup = r.text

# soup = BeautifulSoup(markup, "html.parser")
# print(soup)

# # need to inspect the website you're scraping to find where the data you want it. Class names, html elements etc.
# courses = soup.select(".calendar-event")
# for course in courses:
#   if "Python" in course.h1.text:
#     print(course.h1.text)
#     print(course.h2.text)
#     print('')
#     print('')
