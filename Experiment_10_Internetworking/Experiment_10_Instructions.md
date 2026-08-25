# Experiment 10: Internetworking with Routers, Wireless, and DHCP

## Objective
Design and configure an internetwork using routers, a wireless router, a DHCP server, and an internet cloud.

## Instructions
1. **Wireless Router Setup**:
   - Change SSID to `HomeNetwork`.
   - Set Security Mode to `WEP` and set a key.
   - Configure the internet connection to obtain IP automatically or set a static IP for the WAN port.
2. **DHCP Server Configuration**:
   - Connect a generic Server to the network.
   - In the Services tab -> DHCP -> turn it ON.
   - Set Default Gateway, DNS Server, Start IP, and Subnet Mask.
3. **Client Configuration**:
   - On a Laptop, replace the Ethernet module with a Wireless WPC300N module.
   - Connect to `HomeNetwork` using the WEP key.
   - Set IP configuration to DHCP and verify it receives an IP from the pool.
4. **Internet Cloud**:
   - Connect the Cloud to a Cable Modem and a remote Server (`Cisco.com`).
   - Configure DNS on the remote server to map `Cisco.com` to its IP.
