from unittest import result
from serpapi import GoogleSearch

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

params = {
  "engine": "google",
  "ijn": "0",
  "q": "minecraft shader",
  "google_domain": "google.com",
  "tbs": "itp:photos,isz:l",
  "tbm": "isch",
  "api_key": "secret_api_key"
}

search = GoogleSearch(params)
results = search.get_dict()

print(results)

