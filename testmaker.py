# import solution from ps
import requests
from bs4 import BeautifulSoup

URL = "https://www.acmicpc.net/problem/15652"

res = requests.get(URL)

if res.status_code != 200 :
    print("Http request failed...\nResponse status code: " + str(res.status_code))
    exit(0)

soup = BeautifulSoup(res.text, 'html.parser')
samples = soup.select('.sampledata')

samples = [sample.text for sample in samples]

sampleLength = len(samples) // 2
for i in range(sampleLength) :
    print('----- Sample input ' + str(i+1) + ' -----')
    print(samples[2*i])
    print('----- Sample output ' + str(i+1) + ' -----')
    print(samples[2*i + 1])
    