def domain_name(url):
    result = url.split('//')[-1].split('www.')[-1].split('.')[0]
    return result

url = "http://www.google.com"

print(domain_name(url))