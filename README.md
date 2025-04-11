
# 🛡️ CTI Framework Python Scripts

This repository contains a modular collection of Python scripts for performing cyber threat intelligence (CTI) enrichment, IOC analysis, and investigation using popular open-source and commercial APIs.

Each script is placed in a structured directory and focuses on one task: IP enrichment, IOC lookups, malware classification, feed collection, or breach analysis.

---

## 📂 Contents

### 🔍 `enrichment/`
| Script | Purpose |
|--------|---------|
| `shodan_client.py` | Pulls metadata for a target IP from Shodan |
| `abuseipdb_checker.py` | Checks reputation of suspicious IPs using AbuseIPDB |

### 📡 `feeds/`
| Script | Purpose |
|--------|---------|
| `pulsedive_feed.py` | Pulls threat intelligence indicators from PulseDive |
| `intelx_scraper.py` | Searches darknet appearances via IntelX |

### 🧪 `malware_analysis/`
| Script | Purpose |
|--------|---------|
| `intezer_submit.py` | Submits malware hashes to Intezer for classification |

---

## 🔧 Requirements

Install dependencies via:

```bash
pip install requests
```

Each script requires an API key. Replace `"your_api_key_here"` with your actual key in the respective script.

---

## 🚀 Example Usage

```bash
python enrichment/shodan_client.py
python feeds/pulsedive_feed.py
python malware_analysis/intezer_submit.py
```

Each will prompt for input (e.g., IP, domain, or hash) and return structured JSON responses from the threat intelligence API.

---

## 📘 Notes

- You are responsible for using API keys legally and ethically.
- API usage limits or licensing may apply to some services.
- The structure is modular for easy integration into automation pipelines or dashboards.

---

## 📁 Structure

```
CTI_Framework/
├── enrichment/
│   ├── abuseipdb_checker.py
│   └── shodan_client.py
├── feeds/
│   ├── intelx_scraper.py
│   └── pulsedive_feed.py
├── malware_analysis/
│   └── intezer_submit.py
├── README.md
```

---

Happy hunting 🕵️‍♂️
