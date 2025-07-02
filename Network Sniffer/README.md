# Python Network Packet Sniffer

This project is a simple Python-based network packet sniffer that captures live network traffic and displays useful information about each packet.  
It helps you understand how data flows through a network and the basic structure of protocols like IP, TCP, and TLS.

## 📌 Features

- Captures network packets in real-time
- Extracts and displays:
  - Source and destination IP addresses and ports
  - Protocol used (e.g., TCP)
  - Basic payload details (length)
- Demonstrates TCP handshakes and encrypted HTTPS traffic

## ⚙️ Technologies Used

- **Python 3**
- [Scapy](https://scapy.readthedocs.io/en/latest/) (for packet capturing and analysis)

## 🏃‍♂️ How to Run

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd <project-folder>

2. **Install dependencies**

 pip install -r requirements.txt

3. **Run the sniffer script with root/admin privileges (needed for raw sockets)**
sudo python sniffer.py


4. **Observe output**
The script will print packet information to the console, including:

Source/Destination IPs and ports

Protocol

Payload length

📝 **Example Output**

Source: 192.168.1.6:51156
Destination: 20.42.65.91:443
Protocol: TCP
Raw Payload: 517 bytes

✅ Learning Outcomes
Understand network packet structure (IP, TCP, TLS)

Learn basics of packet capturing and analysis

Experience how encrypted data flows through HTTPS