import requests

my_projects = requests.get('https://api.github.com/users/thapaji/repos').json()
for project in my_projects:
    print(f'Name : {project['name']}\nUrl:{project['url']}\nAuthor:'
          f'{project['owner']['login']}\nProfile URL:{project['owner']['url']}'
          f'\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
