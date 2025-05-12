"""Q.3)Create list of urls and you need to filter out only those that start with 'https'

for Example:

 urls = [

 "http://example.com",

 "https://secure-site.com",

 "ftp://files.example.org",

 "https://another-secure-site.com" """

urls = [
    "http://example.com",
    "https://demo.com",
    "https://secure-site.com",
    "https://site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
]

https_urls = []

for url in urls:
    if url.startswith("https"):
        https_urls.append(url)

for i in https_urls:
    print(i)
