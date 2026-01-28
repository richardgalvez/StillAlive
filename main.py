import requests

sites = ["https://richardgalvez.com",
         "https://google.com/dsacxzcqqc",
         "https://zgopggle12.org",
         "https://chatgpt.com/freegptforlife"]

def check_site(sitename: str):
    try:
        status_code = requests.get(sitename).status_code
    except requests.exceptions.ConnectionError:
        return f"{sitename} - Connection Failed - Site Name Incorrect or Does Not Exist."

    if status_code == 200:
        return f"{sitename} - {status_code} - Site is Up"
    else:
        return f"{sitename} - {status_code} - Site Not Accessible"

for site in sites:
    print(check_site(site))
