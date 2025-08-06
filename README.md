# 🛡️ Phishing Simulation Tool (Educational Use Only)

This is a **safe phishing simulation tool** built with **Python (Flask)**.  
It demonstrates how phishing attacks can capture form input **in a controlled, local environment** for **training and cybersecurity awareness**.

⚠ **Disclaimer**:  
This project is **strictly for educational purposes**.  
Do **NOT** use it on real accounts, real websites, or without explicit permission.  
The author is **not responsible** for any misuse.

---

## 📌 Features
- Simulates a login page and captures **dummy credentials**.
- Logs data to `captured.csv` in a **proper CSV table format**.
- Runs locally in Termux, VS Code, or any Python environment.
- Easy to customize for awareness training.

---


---

## ⚙ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Bagavathisingh/PhisingTool_FreeFire_Page.git
cd PhisingTool_FreeFire_Page
```
## install the requirements using the below command
```bash
pip install -r requirements.txt
```

## Run the Simulation Server Using Below Command

```bash
python server.py
```
## After Run the server.py the terminal Belike :
```bash
 * Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
127.0.0.1 - - [06/Aug/2025 23:59:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Aug/2025 23:59:10] "POST /login HTTP/1.1" 200 -
```
