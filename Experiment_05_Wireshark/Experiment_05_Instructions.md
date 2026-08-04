# Experiment 5: Packet Capture with Wireshark

## Objective
Use Wireshark to capture network packets and understand information encapsulation across protocol layers.

## Instructions
1. **Launch Wireshark**: Select the active network interface (e.g., Wi-Fi or Ethernet).
2. **Capture Packets**: Start the capture. Open a browser and visit a website to generate traffic.
3. **Filtering**:
   - Type `http` to see HTTP traffic.
   - Type `dns` to filter DNS queries.
   - Type `tcp.port == 80` for specific port traffic.
4. **Packet Analysis**:
   - Select a packet and inspect the 'Packet Details' pane.
   - Observe the Frame (Physical Layer), Ethernet II (Data Link), IPv4 (Network), and TCP/UDP (Transport) headers.
5. **Follow TCP Stream**: Right-click a TCP packet -> Follow -> TCP Stream to view the full conversation.
