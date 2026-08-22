# Experiment 9: Subnetting in Packet Tracer

## Objective
Implement classless IP subnetting and configure routers/switches in Packet Tracer.

## Scenario
Given a Class C network `192.168.1.0/24`, subnet it to provide at least 5 hosts per subnet.

## Calculation
- Subnet mask `/27` provides 8 subnets, each with 30 usable hosts.
- Custom Subnet Mask: `255.255.255.224`

## Configuration Steps
1. **Router Configuration**:
   ```text
   Router> enable
   Router# configure terminal
   Router(config)# interface FastEthernet0/0
   Router(config-if)# ip address 192.168.1.1 255.255.255.224
   Router(config-if)# no shutdown
   ```
2. **PC Configuration**:
   - PC1 IP: `192.168.1.11` | Subnet: `255.255.255.224` | Gateway: `192.168.1.1`
   - PC2 IP: `192.168.1.12` | Subnet: `255.255.255.224` | Gateway: `192.168.1.1`
3. **Verification**:
   - Ping from PC1 to PC2 and Router to verify subnet connectivity.
