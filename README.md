# Mini Intrusion Detection System (IDS)

A lightweight Network Intrusion Detection System developed using Python and Scapy.  
This project captures network packets and detects suspicious activities such as SYN scans and packet flooding attacks.

## Features

- Real-time packet sniffing
- SYN scan detection
- Packet flood detection
- Alert logging system
- Modular architecture

## Technologies Used

- Python
- Scapy
- Networking (TCP/IP)

## Project Structure

src/ → core IDS code  
logs/ → alert logs  
screenshots/ → demo images  
docs/ → project documentation

## Installation

pip install -r requirements.txt

## Run the Project

python src/ids.py

## Example Alert

⚠ Possible SYN Scan Detected

## Future Improvements

- Machine learning detection
- Web dashboard
- Email alerts
- Automatic IP blocking
