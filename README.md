# CodeAlpha_Network_Sniffer_TASK-1

# Overview  
This repository contains the code for a simple yet effective Command Line Interface (CLI) Network Packet Analyzer, developed as part of Task 1 during my cybersecurity internship at CodeAlpha. The tool provides a streamlined way to inspect network traffic in real-time.  

# Requirements 
- Python 3.x  
- Root/Administrator Privileges  
- Linux Operating System  
- Typer 0.9.0  

# Features  
✔ Capture and analyze network packets  
✔ Display detailed packet information (IPv6, TCP, UDP, ICMP)  
✔ Extract HTTP request data  
✔ Lightweight and easy to use  

# Usage
Clone the repository to your local machine and execute the following commands:  

# Packet Sniffing Mode: 
Captures live network traffic and displays packet details in real-time.  

```bash
sudo python main.py sniffpackets
```

# HTTP Listener Mode:  
Monitors and logs incoming HTTP requests.  

```bash
sudo python main.py httpmonitor
```

# Useful Resources
- [Typer Documentation](https://typer.tiangolo.com/)  
- [Python Network Programming Guide](https://www.youtube.com/watch?v=WGJC5vT5YJo&list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed&index=1)  
- [Advanced Packet Sniffer in Python](https://systemweakness.com/creating-an-advanced-network-packet-sniffer-in-python-a-step-by-step-guide-9fe51e781c64)  

# Contributing
If you encounter any bugs or have ideas for enhancements, feel free to open an issue or submit a pull request. Your contributions are always welcome!  

