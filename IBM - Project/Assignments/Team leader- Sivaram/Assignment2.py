import requests

place = input('input the city name')
print(place)

print('Displaying Weather report for: ' + place)

url = 'https://wttr.in/{}'.format(place)
res = requests.get(url)

print(res.text)

a= int(input("Please enter the Humidity value :"))
b= int(input("Please enter the temperature value  :"))
c=print(a,b)
print(c)

if a == 36.5:
    print("Due to Temperature report you are in normal days")
if a < 36:
        print("your Temperature is low compare to normal days")
if a > 36:
            print("your Temperature is high compare to normal days")
if b == 55:
    print("Due to Humidity report you are in normal place")
if b < 55:
        print("your Humidity is low compare to normal days")
if b > 55:
            print("your Humidity is high compare to normal days")