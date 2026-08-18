# Experiment 8: NMAP Live Host Discovery

## Objective
Use Nmap to discover live hosts using ARP, ICMP, and TCP/UDP scanning techniques.

## Techniques
1. **ARP Scan (`-PR`)**: Used on local subnets. Nmap sends ARP requests. If a host replies with an ARP response, it's alive.
2. **ICMP Scan (`-PE`, `-PP`, `-PM`)**: 
   - `-PE`: ICMP Echo Request.
   - `-PP`: ICMP Timestamp Request (bypasses some firewalls).
   - `-PM`: ICMP Address Mask Request.
3. **TCP SYN Ping (`-PS`)**: Sends a TCP SYN packet to a port (default 80). If the host replies with SYN/ACK or RST, it is alive.
4. **TCP ACK Ping (`-PA`)**: Sends a TCP ACK packet. Requires root privileges.
5. **UDP Ping (`-PU`)**: Sends a UDP packet. If the port is closed, an ICMP "Port Unreachable" is returned, indicating the host is up.

## Example Commands
```bash
# ARP ping scan on a local subnet
nmap -PR -sn 192.168.1.0/24

# TCP SYN ping on specific ports without port scanning
nmap -PS22,80,443 -sn 10.10.10.0/24
```
