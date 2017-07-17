from urllib.parse import urlencode, quote_plus

payload = {'username':'administrator', 'password':'xyz das dasdd'}
result = urlencode(payload, quote_via=quote_plus)
print(result)
