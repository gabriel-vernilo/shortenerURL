import pyperclip
from urllib.request import urlopen

url = str(input('\nenter url : '))
tiny_req = f'https://tinyurl.com/api-create.php?url={url}'
url_res = urlopen(tiny_req)
short_url = url_res.read().decode()
print(f'\nshortened url : {short_url}')
url_clipboard = pyperclip.copy(short_url)
print('\nurl copied to clipboard')