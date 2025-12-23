# URL Monitor - Website Status Checker

Monitor website availability and receive desktop notifications for status changes.

## Description

Checks a list of URLs, prints status codes, and optionally shows Windows toast notifications via win10toast.

## Features

- HTTP status checks with timeout
- Optional Windows toast notifications (win10toast optional dependency)
- Console output fallback when notifications are unavailable
- Basic SSL warning suppression for self-signed endpoints

## Prerequisites

- Python 3.8+
- Windows 10/11 for toast notifications (console works everywhere)
- Internet connection

## Installation

```bash
pip install requests win10toast
```

## Usage

```bash
python checkurl.py
```

The script checks the predefined URLs and prints status. If win10toast is installed, it shows a toast per URL indicating online/offline.

## Configuration

- Edit `URLs` in the script to add or remove endpoints.
- SSL verification is disabled in the script for compatibility; enable verification in production.
- To monitor continuously, wrap the check loop with a sleep interval.

## Dependencies

| Package    | Purpose                      |
|------------|------------------------------|
| requests   | HTTP requests with timeouts  |
| win10toast | Windows toast notifications  |
| urllib3    | Warning suppression          |

## Notes

- Keep the number of monitored URLs reasonable to avoid rate limits.
- Re-enable SSL verification for production systems.

---

Part of the [Python Projects Collection](../README.md)
