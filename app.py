from flask import Flask, request, render_template
import subprocess
import xml.etree.ElementTree as ET

app = Flask(__name__)

def run_nmap_scan(target):
    try:
        result = subprocess.run(
            ["nmap", "-sV", "-oX", "-", target], 
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return None

def parse_nmap_xml(xml_output):
    root = ET.fromstring(xml_output)
    ports = []
    for host in root.findall('host'):
        for port in host.find('ports').findall('port'):
            port_info = {
                'port': port.get('portid'),
                'state': port.find('state').get('state'),
                'service': port.find('service').get('name')
            }
            ports.append(port_info)
    return ports

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    xml_output = run_nmap_scan(target)
    if xml_output:
        open_ports = parse_nmap_xml(xml_output)
        return render_template('results.html', target=target, open_ports=open_ports)
    else:
        return render_template('results.html', target=target, open_ports=[], error="Unable to connect to the target or invalid target.")

if __name__ == '__main__':
    app.run(debug=True)
