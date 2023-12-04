import requests
import csv
import concurrent.futures
import threading

proxylist = []
results = []
print_lock = threading.Lock()

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    result = {'proxy': proxy, 'status': ''}
    try:
        r = requests.get('https://www.hiperlibertad.com.ar', proxies={'http': proxy, 'https': proxy}, timeout=5)
        r.raise_for_status()
        result['status'] = 'Works'
    except requests.exceptions.RequestException as e:
        result['status'] = f'Error: {e}'
    
    with print_lock:
        results.append(result)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)

# Escribir los resultados en un archivo CSV
header = ['proxy', 'status']
with open('proxy_results.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(results)
