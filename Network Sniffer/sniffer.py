from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    print("=" * 50)
    
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        
        if TCP in packet:
            print("TCP Packet")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print("UDP Packet")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print("ICMP Packet")
        
        if packet.haslayer(Raw):
            print(f"Payload: {packet[Raw].load}")
        else:
            print("No Raw Payload")
    else:
        print("Non-IP Packet")

if __name__ == '__main__':
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=False, filter="ip") 
