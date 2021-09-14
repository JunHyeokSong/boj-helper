import requests
from bs4 import BeautifulSoup

def getResponse(url) : 
    res = requests.get(url)
    if res.status_code != 200 :
        print("Http request failed...\nResponse status code: " + str(res.status_code))
        exit(0)
    return res
    
def extractSamples(text) :
    soup = BeautifulSoup(text, 'html.parser')
    samples = soup.select('.sampledata')
    samples = [sample.text for sample in samples]
    sampleInputs = [samples[i] for i in range(len(samples)) if i % 2 == 0]
    sampleOutputs = [samples[i] for i in range(len(samples)) if i % 2 == 1]
    return sampleInputs, sampleOutputs