import requests
import csv
import concurrent.futures
import threading

proxylist = []
print_lock = threading.Lock()

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])
        
def extract(proxy):
    try:
        r = requests.get('https://www.hiperlibertad.com.ar', proxies={'http': proxy, 'https': proxy}, timeout=5)
        with print_lock:
            print(f'{proxy} | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)
    
#print(proxylist)