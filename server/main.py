import requests
import ipaddress
from queue import Queue
from threading import Thread

def get_report(ip:str, port:int) -> None:
    ip_addr = f'http://{ip}:{port}'
    response = requests.get(ip_addr)

    with open(f'{ip}.txt', 'w') as file:
        file.write(response.text)

def find_clients(ip_range:str, client_port:int) -> Queue:
    q = Queue()
    res_q = Queue()
    th_size = 256

    for ip in ipaddress.IPv4Network(ip_range):
        q.put((ip, client_port))

    for i in range(th_size):
        t = Thread(target=worker, args=[q, res_q])
        t.daemon = True
        t.start()

    q.join()
    return res_q

def worker(q:Queue, result_q:Queue):
    ip, port = q.get()

    if make_ping(ip, port):
        result_q.put((ip, port))

    q.task_done()


def make_ping(ip:str, port:int) -> bool:
    ip_addr = f'http://{ip}:{port}/ping'
    try:
        response = requests.get(ip_addr, timeout=2)

        if response.text == "ping":
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False


result = find_clients("192.168.1.0/24", 5000)

while not result.empty():
    ip, port = result.get()
    print(ip, port)
    get_report(ip, port)

print("done")


