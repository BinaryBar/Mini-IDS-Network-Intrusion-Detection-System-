from scapy.all import *
from collections import defaultdict
from config import PACKET_THRESHOLD
from logger import log_alert

ip_counter = defaultdict(int)

def analyze_packet(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src

        ip_counter[src_ip] += 1

        if ip_counter[src_ip] > PACKET_THRESHOLD:

            log_alert(f"Possible Flood Attack from {src_ip}")

    if packet.haslayer(TCP):

        flags = packet[TCP].flags

        if flags == "S":

            log_alert("Possible SYN Scan Detected")