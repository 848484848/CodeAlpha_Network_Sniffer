#!/usr/bin/env python3
from scapy.all import *

# This function will handle each packet that is captured
def packet_handler(pkt):
    if pkt.haslayer(IP):  # Check if the packet has an IP layer
        ip_src = pkt[IP].src   # Source IP address
        ip_dst = pkt[IP].dst   # Destination IP address
        print(f"IP Packet: {ip_src} -> {ip_dst}")

        if pkt.haslayer(TCP):  # If the packet is TCP
            tcp_src_port = pkt[TCP].sport
            tcp_dst_port = pkt[TCP].dport
            print(f"TCP Packet: {tcp_src_port} -> {tcp_dst_port}")
        elif pkt.haslayer(UDP):  # If the packet is UDP
            udp_src_port = pkt[UDP].sport
            udp_dst_port = pkt[UDP].dport
            print(f"UDP Packet: {udp_src_port} -> {udp_dst_port}")

        # You can add more layers to analyze (e.g., HTTP, DNS, etc.)
    else:
        print("Non-IP Packet Captured")

# Start sniffing the network
def start_sniffing(interface="eth0"):
    print(f"Starting packet capture on interface {interface}...")
    sniff(iface=interface, prn=packet_handler, store=0)

if __name__ == "__main__":
    start_sniffing()
