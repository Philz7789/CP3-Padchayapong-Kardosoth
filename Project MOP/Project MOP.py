import requests
import datetime
import time

def main(message):
    url_line = 'https://notify-api.line.me/api/notify'
    token = 'Xtpnr0CdzOAfNtfkPk9ZF9RZ8f0XYTQyJXsc4ws9Qa6'
    header = {'content-Type': 'application/x-www-form-urlencoded',
              'Authorization': 'Bearer ' + token}
    session = requests.Session()
    return session.post(url_line, headers=header, data=msg)

key_metalprice = ("https://api.metalpriceapi.com/v1/"
                  "latest?api_key=a1467ab89ac994c5325a97c2520a16f1&base"
                  "=XAU&currencies=USD")
data = requests.get(key_metalprice)
data = data.json()
price = (f"{data['base']}/,{data['rates']}")

msg = {'message': price}

#set the duration for the price_text sending to line notification
end_time = datetime.datetime.now() + datetime.timedelta(seconds=14400)

while datetime.datetime.now() < end_time:
    main(msg)
    time.sleep(600)