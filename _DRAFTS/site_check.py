import requests, sys, socket, whois


url = 'https://vk.com' # добавить возможность проверки валидности ЮРЛ + добавление нескольких(множества) юрл


page = requests.get(url)

print(f'File :: {__file__} | SYS :: {sys.version}')
#print(sys.argv)

print(f'\nPAGE STATUS :: {page.status_code}')

#print(socket.gethostbyname('habr.com'))

print('')
print(f'{url}')

surl =  url.split('/')
print(surl)
print(surl[2])

print(socket.gethostbyname(surl[2])) # Добавить функцию проверки домен / www.домен + сравнение IP и выделение цветом.

print('')

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(f'Me :: {get_location()}')
print('')

w = whois.whois(surl[2])
print(f'WHOIS :: {w}')
