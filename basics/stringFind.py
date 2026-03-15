bl =b'GET /light/on HTTP/1.1\r\nHost: 10.245.74.48\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-AU,en-US;q=0.9,en-GB;q=0.8,en;q=0.7\r\n\r\n'

s = bl.decode("utf-8")
print (s)

f = s.find("/light/on")
print (f)