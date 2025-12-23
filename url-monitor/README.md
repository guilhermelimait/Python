# 🔍 URL Monitor - Website Status Checker

Monitor website availability and receive desktop notifications for status changes.

## 📝 Description

A Python utility that checks website HTTP status codes and sends Windows desktop notifications when sites go online or offline. Perfect for monitoring critical services or waiting for website availability.

## ✨ Features

- **HTTP Status Checking**: Real-time website availability monitoring
- **Desktop Notifications**: Windows 10/11 toast notifications
- **Custom URLs**: Monitor any website or endpoint
- **Status Code Detection**: Identify specific HTTP response codes
- **SSL Verification**: Optional SSL certificate verification

## 📋 Prerequisites

- Python 3.8+
- Windows 10/11 (for toast notifications)
- Internet connection

## 📦 Installation

```bash
# Install required packages
pip install requests win10toast
```

## 🚀 Usage

### Basic Usage

```bash
python checkurl.py
```

### Script Functionality

The script monitors specified URLs and displays notifications:

```python
import requests
import win10toast

t = win10toast.ToastNotifier()

response = requests.get("https://example.com", verify=False)
result = response.status_code

if result == 200:
    t.show_toast("Alert", "SITE ONLINE\nWebsite is available", "icon.ico", 10)
if result == 406:
    t.show_toast("Alert", "SITE DOWN\nWebsite is unavailable", "icon.ico", 10)
```

## 🔧 Configuration

### Monitor Multiple URLs

Edit the script to add your URLs:

```python
urls = [
    "https://example.com",
    "https://api.myservice.com",
    "https://mywebsite.com/health"
]

for url in urls:
    response = requests.get(url, verify=False)
    # Add notification logic
```

### Continuous Monitoring

Add a loop for periodic checking:

```python
import time

while True:
    # Check URLs
    check_websites()
    time.sleep(300)  # Check every 5 minutes
```

## 📊 HTTP Status Codes

| Code | Meaning | Notification |
|------|---------|--------------|
| 200 | OK | Site is online |
| 404 | Not Found | Page missing |
| 500 | Server Error | Server issue |
| 503 | Service Unavailable | Service down |

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| requests | 2.31.0+ | HTTP requests |
| win10toast | Latest | Windows notifications |
| clear_screen | Custom | Console clearing |

## 💡 Use Cases

- **Service Monitoring**: Track critical service availability
- **Website Launches**: Get notified when new sites go live
- **API Monitoring**: Check API endpoint health
- **Downtime Alerts**: Immediate notification of outages

## ⚙️ Advanced Features

### Add Logging

```python
import logging

logging.basicConfig(filename='url_monitor.log', level=logging.INFO)
logging.info(f'URL: {url} - Status: {status_code}')
```

### Email Notifications

Combine with SMTP for email alerts:

```python
import smtplib
# Send email when status changes
```

## 🐛 Troubleshooting

**Issue**: SSL Certificate errors
- Set `verify=False` in requests (already configured)
- Install certificate bundle: `pip install certifi`

**Issue**: Notifications not showing
- Check Windows notification settings
- Run script with administrator privileges
- Ensure Python has notification permissions

## ⚠️ Notes

- Disable SSL verification only for testing
- Add delays between requests to avoid rate limiting
- Consider using proper monitoring tools for production

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
