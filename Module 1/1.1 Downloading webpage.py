from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')

html_str = str(html)

print('Python' if html_str.count('Python' or 'python') > html_str.count('C++') else 'C++')
print(html_str)