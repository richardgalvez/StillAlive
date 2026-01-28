# Send HTTP request to site or list of sites

import requests

name = "https://richardgalvez.com"
http_request = requests.get(name).status_code

def check_site(sitename: str, status_code: int):
    if status_code == 200:
        return f"{sitename} - Site is Up!"
    else:
        return f"{sitename} - Site Not Accessible..."

print(check_site(name, http_request))
