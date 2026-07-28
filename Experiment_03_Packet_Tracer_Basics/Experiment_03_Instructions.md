# Experiment 3: CISCO Packet Tracer Basics

## Objective
Understand the environment of CISCO Packet Tracer and analyze the behavior of network devices like HUBs and Switches.

## Instructions
1. **Environment Overview**: Open Packet Tracer. Familiarize yourself with the workspace, logical/physical tabs, and device toolbars.
2. **Design using HUB**:
   - Add a HUB and 4 PCs.
   - Connect PCs to the HUB using Copper Straight-Through cables.
   - Assign static IP addresses (e.g., `10.1.1.1` to `10.1.1.4`).
   - Send a PDU from PC0 to PC1. Observe the HUB broadcasts the packet to all ports.
3. **Design using Switch**:
   - Add a Switch and 4 PCs.
   - Connect PCs to the Switch.
   - Assign static IPs.
   - Send a PDU. Observe the Switch learns MAC addresses and forwards packets only to the destination port.

## Observation
A HUB operates at Layer 1 and broadcasts traffic, causing collisions. A Switch operates at Layer 2, learns MAC addresses, and forwards traffic intelligently.
