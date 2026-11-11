# Lesson 4. library
# import requests
# Код c requests library

# response = requests.get('https://in.uz/me')
# print(response.text)

### Ниже код с использованием json, requsts и HTTP

# import json
# import requests
# import sys

#  if len(sys.argv) != 2:
#    sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])
#
# o = response.json()
# for i in o['results']:
#    print(i[])

### Ниже код с использованием функции из другого файла. В файле functions.py есть функция power_2
# которая возводит число в квадрат.
import functions
i = int(input("Введите число: "))
print(functions.power_2(i))