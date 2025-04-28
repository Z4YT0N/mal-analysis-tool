# Qu1cksc0pe

<div align="center">
   
## 🔍 Overview

Qu1cksc0pe is an All-in-One malware analysis tool with a modern graphical user interface, designed to analyze various file types, from Windows binaries to E-Mail files. It provides comprehensive insights into suspicious files and helps analysts understand their capabilities.

### Key Features

- Modern and intuitive graphical user interface
- DLL dependency analysis
- Function and API extraction
- Section and segment analysis
- URL, IP address, and email detection
- Android permission analysis
- File extension analysis
- Embedded executable/exploit detection

## 📋 Supported File Types

| Files | Analysis Type |
| :--- | :--- |
| Windows Executables (.exe, .dll, .msi, .bin) | Static, Dynamic |
| Linux Executables (.elf, .bin) | Static, Dynamic |
| MacOS Executables (mach-o) | Static |
| Android Files (.apk, .jar, .dex) | Static, Dynamic(APK only) |
| Golang Binaries (Linux) | Static |
| Document Files | Static |
| Archive Files (.zip, .rar, .ace) | Static |
| PCAP Files (.pcap) | Static |
| Powershell Scripts | Static |
| E-Mail Files (.eml) | Static |

## 🛠️ Prerequisites

- Python 3.10 or higher
- Approximately 500MB disk space
- Internet connection (for installation only)
- VirusTotal API Key (for VirusTotal analysis)
- Required tools:
  - Strings
  - Jadx (for Android analysis)
  - PyOneNote
  - Mono (.NET analysis)

## 💻 Installation

### Windows Installation

```powershell
# Clone the repository
git clone --depth 1 https://github.com/CYB3RMX/Qu1cksc0pe

# Navigate to the directory
cd Qu1cksc0pe

# Run the setup script as Administrator
.\setup.ps1

# Install GUI requirements
pip install -r gui_requirements.txt
```

### Linux Installation

```bash
# Clone the repository
git clone --depth 1 https://github.com/CYB3RMX/Qu1cksc0pe

# Create and activate virtual environment
virtualenv -p python3 sc0pe_venv
source sc0pe_venv/bin/activate

# Run setup script
bash setup.sh

# Install GUI requirements
pip install -r gui_requirements.txt
```

### Docker Installation

```bash
docker build -t qu1cksc0pe .
docker run -it --rm -v $(pwd):/data qu1cksc0pe:latest
```

## 🚀 Usage

### Starting the GUI
```bash
python QuickScope_GUI.py
```

## 🔧 Troubleshooting

1. **Module Installation Issues**:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   pip install -r gui_requirements.txt
   ```

2. **Access Issues**:
   - Ensure running with administrator/root privileges
   - Verify `sc0pe_Base` directory exists in user folder

3. **Android Tool Issues**:
   - Verify Android Platform Tools installation
   - Check ADB path in `Systems/Windows/windows.conf`

## 🌟 Recommended Systems

- Windows 10/11
- Parrot OS
- Kali Linux
- Other Linux distributions

## 📝 License

This project is licensed under GPL 3.0

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

# Updates
<b>07/04/2025</b>
- [X] Improvements on ```Windows Dynamic Analyzer``` module.

<b>27/03/2025</b>
- [X] Improvements on ```Windows Dynamic Analyzer``` module. Qu1cksc0pe can now extract ```Telegram Bot Token``` and possible ```Telegram Chat ID``` values.
- [X] With the ```Telegram Bot Token``` and ```Telegram Chat ID```, you can infiltrate Telegram bots using <a href="https://github.com/0x6rss/matkap">Matkap</a>

<b>25/03/2025</b>
- [X] Improvements on ```Windows Dynamic Analyzer``` module.

# Available On
<img width="400" src="https://user-images.githubusercontent.com/42123683/189416163-4ffd12ce-dd62-4510-b496-924396ce77c2.png" alt="logo"><img width="400" src="https://user-images.githubusercontent.com/42123683/189416193-a709291f-be8f-469c-b649-c6201fa86677.jpeg" alt="logo">
<img width="400" src="https://github.com/user-attachments/assets/a555750e-d979-4f0f-9d2c-730662b00915" alt="logo">
<img width="400" src="https://github.com/user-attachments/assets/56054b07-0512-42bb-ab97-cecbf845116e" alt="logo">

# Dynamic Analysis
## Android Application Analysis
> [!NOTE]
> You must connect a virtual device or physical device to your computer.

## Windows Process Analysis

https://github.com/CYB3RMX/Qu1cksc0pe/assets/42123683/a2c84b8f-c12c-47ac-96e9-c345aeda1f54

# References
- <a href="https://www.linkedin.com/posts/mehmetalikerimoglu_qu1cksc0pe-all-in-one-static-malware-analysis-activity-6853239604439523328-B9dN/?trk=public_profile_like_view&originalSubdomain=tr">The Cyber Security Hub</a>
- <a href="https://www.kitploit.com/2021/12/top-20-most-popular-hacking-tools-in.html">Kitploit - Top 20 Most Popular Hacking Tools in 2021</a>
- <a href="https://www.csirt.rnsi.mai.gov.pt/content/infosec-news-20211011">CSIRT.MAI</a>
- <a href="https://vulners.com/kitploit/KITPLOIT:8846405132281597137">Vulners</a>
- <a href="https://www.redpacketsecurity.com/qu1cksc0pe-all-in-one-static-malware-analysis-tool/">RedPacket Security</a>
- <a href="https://cert.bournemouth.ac.uk/qu1cksc0pe-all-in-one-static-malware-analysis-tool/">Bournemouth University - CERT</a>
- <a href="https://github.com/Ignitetechnologies/Mindmap/blob/main/Forensics/Digital%20Forensics%20Tools%20HD.png">Hacking Articles - Digital Forensics Tools Mindmap</a>
- <a href="https://twitter.com/hack_git/status/1666867995036057602">HackGit - Twitter Post</a>
- <a href="https://twitter.com/DailyDarkWeb/status/1668966526358286336">Daily Dark Web - Twitter Post</a>
- <a href="https://isc.sans.edu/diary/The+Importance+of+Malware+Triage/29984">SANS ISC - Blog Post</a>
- <a href="https://korben.info/qu1cksc0pe-analyse-logiciels-malveillants.html">Korben - Blog Post</a>
- <a href="https://www.heise.de/ratgeber/Malware-Analysetool-Schadpotenzial-von-Daten-mit-Qu1cksc0pe-ermitteln-10001929.html">heise online - Blog Post</a>
