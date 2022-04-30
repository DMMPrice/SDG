# importing packages
import requests

# URL
# url = "https://this-person-does-not-exist.com/en"
url = 'https://www.facebook.com/favicon.ico'

r = requests.get(url, allow_redirects=True)
open('facebook.ico', 'wb').write(r.content)