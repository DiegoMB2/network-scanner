import nmap

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.0.0/24', arguments='-sn')

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            ip = nm[host]['addresses']['ipv4']
            mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'][mac]
            print(f"IP: {ip}\tMAC: {mac}\tVendor: {vendor}")
        else:
            ip = nm[host]['addresses']['ipv4']
            print(f"IP: {ip}")

scan_network()
