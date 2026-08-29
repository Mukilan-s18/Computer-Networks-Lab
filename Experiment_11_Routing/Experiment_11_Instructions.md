# Experiment 11: Routing at Network Layer

## Objective
Simulate Static Routing and Dynamic Routing (RIP) using CISCO Packet Tracer.

## Static Routing
Static routes are manually added to the routing table.
```text
Router(config)# ip route <destination_network> <subnet_mask> <next_hop_ip>
Router(config)# ip route 30.0.0.0 255.0.0.0 20.0.0.2 10
```
- The number `10` is the Administrative Distance, useful for backup routes.

## RIP (Routing Information Protocol)
RIP automatically learns and exchanges route information.
```text
Router(config)# router rip
Router(config-router)# network 10.0.0.0
Router(config-router)# network 192.168.1.0
```

## Verification
- Use `show ip route` to view the routing table.
- `S` indicates Static, `R` indicates RIP.
- Use `tracert <ip>` on a PC to trace the path taken by packets.
