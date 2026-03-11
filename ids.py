from scapy.all import sniff
from detector import analyze_packet

def start_ids():

    print("Mini IDS Started... Monitoring Network")

    sniff(prn=analyze_packet, store=0)

if __name__ == "__main__":

    start_ids()