import nmap 

def nmap_default_1():
  nm = nmap.PortScanner()

  ip_range        = "192.168.1.1/24"
  http_ip_list    = []
  http_port_list  = []

  nm.scan(ip_range, arguments="-Pn")
  for host in nm.all_hosts():
      print(host)
  ip_list = ' '.join(nm.all_hosts())

  nm.scan(ip_list,arguments='-sV')
  for ip in nm.all_hosts():
      print(nm.scaninfo())
      if "tcp" in nm[ip]:
          print(nm[ip]['tcp'].keys())
          print("---"*20)
          for port in nm[ip]['tcp'].keys():
              if (nm[ip]['tcp'][port]['name']=="http"):
                  name    = nm[ip]['tcp'][port]['name']
                  product = nm[ip]['tcp'][port]['product']
                  version = nm[ip]['tcp'][port]['version']
                  print(ip,port,name,product,version)
                  if ip not in http_ip_list:
                      http_ip_list.append(ip)
                  if port not in http_port_list:
                      http_port_list.append(port)

  print("##########")
  print(http_ip_list)
  print(http_port_list)
  
nmap_default_1()
