import asyncio
import httpx

sites = ["https://richardgalvez.com",
         "https://google.com/dsacxzcqqc",
         "https://amazon.com",
         "https://zgopggle12.org",
         "https://linkedin.com",
         "https://chatgpt.com/freegptforlife",
         "https://youtube.com",
         "https://github.com",
         "https://robotoverlords.gov"]

def check_site(sitename: str):
    try:
        status_code = httpx.get(sitename).status_code
    except httpx.RequestError as e:
        return f"{sitename} - Connection Failed - Site Name Incorrect or Does Not Exist. ExceptionError: {e}"

    if status_code == 200:
        return f"{sitename} - {status_code} - Site is Up"
    else:
        return f"{sitename} - {status_code} - Site Not Accessible"

# for site in sites:
#     print(check_site(site))

async def main():
    async with httpx.AsyncClient() as client:
        for site in sites:
            try:
                response = await client.get(site)
                print(response.status_code)
            except httpx.RequestError as e:
                print(f"{site} - Connection Failed - Site Name Incorrect or Does Not Exist. ExceptionError: {e}")

asyncio.run(main())
