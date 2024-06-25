import socket
import nmap
import requests
from requests.exceptions import RequestException

def check_open_ports(target, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error as e:
            open_ports.append(f"Error: {e}")
    return open_ports

def check_http_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        vulnerabilities = []
        if 'Server' in headers:
            vulnerabilities.append(('Server Header', headers['Server']))
        if 'X-Powered-By' in headers:
            vulnerabilities.append(('X-Powered-By Header', headers['X-Powered-By']))
        return vulnerabilities
    except RequestException as e:
        return [f"HTTP request error: {e}"]

def detailed_scan(target):
    try:
        nm = nmap.PortScanner()
        nm.scan(target, '1-1024', '-sV')
        scan_data = {}
        for host in nm.all_hosts():
            scan_data[host] = nm[host]
        return scan_data
    except nmap.PortScannerError as e:
        return [f"Nmap scan error: {e}"]
    except Exception as e:
        return [f"Unexpected error during Nmap scan: {e}"]

def scan_target(target):
    results = {
        "open_ports": [],
        "http_vulnerabilities": [],
        "detailed_results": {}
    }

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror as e:
        return {'error': f"Error resolving target: {e}"}

    common_ports = [21, 22, 23, 25, 80, 110, 143, 443, 8080]
    open_ports = check_open_ports(target_ip, common_ports)

    url = f"http://{target}" if not target.startswith('http') else target
    http_vulnerabilities = check_http_headers(url)

    detailed_results = detailed_scan(target_ip)

    return {
        'open_ports': open_ports,
        'http_vulnerabilities': http_vulnerabilities,
        'detailed_results': detailed_results
    }
