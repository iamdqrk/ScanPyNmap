import nmap

target = '10.0.0.61' #set your target ip here
port = '22' #set your target port here

nm = nmap.PortScanner()
nm.scan(hosts=target, ports=port)
if nm.all_hosts():
    print('Host found')
    for host in nm.all_hosts():
        hostip = host
        host_state = nm['host_ip'].state()
        port_state = nm['host_ip']['tcp'][port]['state']
        print(f'{host_ip} - {host_state} - {port_state}')
else: 
    print('Host not found')



