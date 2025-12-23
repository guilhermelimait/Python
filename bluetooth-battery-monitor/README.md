# 🎧 Bluetooth Battery Monitor

Monitor and check battery levels of Bluetooth headsets and devices connected to your Windows PC.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📝 Description

A comprehensive Python utility that monitors Bluetooth device battery levels on Windows. Uses multiple detection methods to ensure maximum compatibility with different Bluetooth headsets, earbuds, and audio devices.

## ✨ Features

- 🔍 **BLE Device Scanning**: Discover nearby Bluetooth Low Energy devices
- 🔋 **Battery Level Detection**: Read battery percentage from compatible devices
- 💻 **Multiple Detection Methods**: 4 different approaches for maximum compatibility
- 🎯 **Interactive Menu**: Easy-to-use command-line interface
- 📊 **Real-time Monitoring**: Check battery status on demand
- 🪟 **Windows Integration**: PowerShell and WMI support
- 🎨 **Beautiful Output**: Color-coded, emoji-rich console display

## 🔧 Detection Methods

### 1. **BLE (Bluetooth Low Energy)** 🔵
Uses the standard Bluetooth Battery Service to read battery levels directly from devices.
- **UUID**: `0000180f-0000-1000-8000-00805f9b34fb`
- **Best for**: Modern Bluetooth 4.0+ devices
- **Accuracy**: High

### 2. **PowerShell Integration** 💻
Queries Windows Bluetooth device properties via PowerShell.
- **Best for**: Windows 10/11 paired devices
- **Accuracy**: Medium

### 3. **WMI (Windows Management)** 🖥️
Lists Bluetooth devices through Windows Management Instrumentation.
- **Best for**: System-level device information
- **Accuracy**: Medium

### 4. **Windows Bluetooth API** 🪟
Direct Windows Bluetooth API queries.
- **Best for**: Native Windows Bluetooth stack
- **Accuracy**: Varies

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **Operating System**: Windows 10/11
- **Bluetooth**: Built-in or USB Bluetooth adapter
- **Devices**: Bluetooth headset/earbuds that support Battery Service

## 📦 Installation

### Quick Install

```bash
# Navigate to the folder
cd bluetooth-battery-monitor

# Install dependencies automatically
python battery_monitor.py --install
```

### Manual Install

```bash
pip install bleak wmi psutil
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| bleak | Latest | BLE device scanning and connection |
| wmi | Latest | Windows Management Instrumentation |
| psutil | Latest | System utilities |

## 🚀 Usage

### Basic Usage

```bash
python battery_monitor.py
```

### Menu Options

When you run the script, you'll see an interactive menu:

```
📋 Select Method:

1. 🔍 Scan for BLE devices and check battery
2. 💻 Use PowerShell to check battery
3. 🖥️  Use WMI to list Bluetooth devices
4. 🪟 Use Windows API
5. 🔄 Try all methods
6. ❌ Exit
```

### Step-by-Step Guide

1. **Run the script**: `python battery_monitor.py`
2. **Choose method**: Select option `1` for BLE scan (most reliable)
3. **Wait for scan**: Script will discover nearby Bluetooth devices
4. **Select device**: Choose your headset from the list
5. **View battery**: Battery percentage will be displayed

### Example Output

```
🔍 Scanning for Bluetooth devices...
  📱 Found: Sony WH-1000XM4 (AA:BB:CC:DD:EE:FF)
  📱 Found: AirPods Pro (11:22:33:44:55:66)

Select a device to check battery:
  1. Sony WH-1000XM4 (AA:BB:CC:DD:EE:FF)
  2. AirPods Pro (11:22:33:44:55:66)

👉 Enter device number: 1

🔋 Checking battery for: Sony WH-1000XM4
✅ Connected!

────────────────────────────────────────
🎧 Device: Sony WH-1000XM4
🔋 Battery: 85%
────────────────────────────────────────
```

## 🎯 Compatible Devices

### ✅ Confirmed Working
- Sony WH-1000XM3/XM4/XM5
- Apple AirPods (Pro, Max, 1st/2nd/3rd gen)
- Bose QuietComfort series
- Jabra Elite series
- Samsung Galaxy Buds
- Microsoft Surface Headphones
- Most modern Bluetooth 4.0+ headphones

### ⚠️ May Not Work
- Very old Bluetooth devices (pre-4.0)
- Devices without Battery Service support
- Some proprietary Bluetooth implementations

## 💡 Use Cases

- 🎵 **Music Lovers**: Check headphone battery before long listening sessions
- 🎮 **Gamers**: Monitor gaming headset battery during gameplay
- 💼 **Remote Workers**: Ensure headset is charged for meetings
- 🏃 **Fitness**: Check earbud battery before workouts
- 🛠️ **Tech Support**: Diagnose Bluetooth device issues
- 📊 **Battery Tracking**: Log battery levels over time

## 🔧 Advanced Features

### Run All Methods at Once

```bash
# Select option 5 from menu
python battery_monitor.py
👉 Enter your choice: 5
```

This will try all 4 detection methods sequentially, useful for:
- Testing compatibility
- Troubleshooting connection issues
- Finding the best method for your device

### Programmatic Usage

```python
import asyncio
from battery_monitor import BluetoothBatteryChecker

async def check_battery():
    checker = BluetoothBatteryChecker()
    
    # Scan for devices
    devices = await checker.scan_bluetooth_devices()
    
    # Check first device battery
    if devices:
        battery = await checker.get_battery_level_ble(devices[0]['address'])
        print(f"Battery: {battery}%")

asyncio.run(check_battery())
```

## 🐛 Troubleshooting

### Issue: "Bleak not installed"
**Solution**: Run `python battery_monitor.py --install` or `pip install bleak`

### Issue: "No devices found"
**Solution**:
- Ensure Bluetooth is enabled on your PC
- Make sure device is powered on and in pairing mode
- Check Windows Settings → Bluetooth & devices
- Try moving device closer to PC

### Issue: "Could not read battery level"
**Solution**:
- Device may not support Battery Service
- Try pairing device first in Windows Settings
- Some devices only show battery when actively connected
- Try different detection methods (option 5)

### Issue: "Connection timeout"
**Solution**:
- Ensure device is not connected to another device
- Restart Bluetooth adapter
- Try re-pairing the device
- Check for Windows updates

### Issue: "Permission denied"
**Solution**:
- Run PowerShell as Administrator
- Check Windows Bluetooth permissions
- Ensure Python has Bluetooth access

## ⚙️ Configuration

### Increase Scan Timeout

Edit `battery_monitor.py`:
```python
# Line ~50
devices = await BleakScanner.discover(timeout=20.0)  # Increase from 10 to 20 seconds
```

### Change Connection Timeout

```python
# Line ~75
async with BleakClient(address, timeout=30.0) as client:  # Increase timeout
```

## 📊 Technical Details

### Bluetooth Battery Service

The script uses the standard Bluetooth Battery Service specification:
- **Service UUID**: `0000180f-0000-1000-8000-00805f9b34fb`
- **Characteristic UUID**: `00002a19-0000-1000-8000-00805f9b34fb`
- **Data Format**: Single byte (0-100)

### Platform Support

| Feature | Windows 10 | Windows 11 | macOS | Linux |
|---------|-----------|-----------|-------|-------|
| BLE Scan | ✅ | ✅ | ⚠️ | ⚠️ |
| PowerShell | ✅ | ✅ | ❌ | ❌ |
| WMI | ✅ | ✅ | ❌ | ❌ |
| Windows API | ✅ | ✅ | ❌ | ❌ |

*Note: Script is optimized for Windows. macOS/Linux support would require modifications.*

##  Related Projects

- [bleak](https://github.com/hbldh/bleak) - Bluetooth Low Energy platform library
- [pybluez](https://github.com/pybluez/pybluez) - Bluetooth Python extension
- [Windows Bluetooth API](https://docs.microsoft.com/en-us/windows/uwp/devices-sensors/bluetooth)

## 🔒 Privacy & Security

- ✅ **Local Only**: All operations are performed locally
- ✅ **No Data Collection**: Script doesn't send data anywhere
- ✅ **Read-Only**: Only reads battery information
- ✅ **Open Source**: Full source code available for review

## ⚠️ Limitations

1. **Device Compatibility**: Not all Bluetooth devices expose battery information
2. **Windows Only**: Currently optimized for Windows 10/11
3. **Active Connection**: Some methods require active Bluetooth connection
4. **Administrator Rights**: Some features may require elevated permissions
5. **Battery Service**: Device must support Bluetooth Battery Service standard

## 📖 Resources

- [Bluetooth Battery Service Specification](https://www.bluetooth.com/specifications/gatt/services/)
- [Windows Bluetooth Documentation](https://docs.microsoft.com/en-us/windows-hardware/drivers/bluetooth/)
- [Python Bleak Documentation](https://bleak.readthedocs.io/)

## 📄 License

MIT License - Feel free to use and modify for your projects.

## 🙏 Acknowledgments

- **Bleak Team**: For excellent BLE library
- **Python Community**: For WMI and system libraries
- **Bluetooth SIG**: For Battery Service specification

---

## 📞 Support

**Issues or Questions?**
- Check the [Troubleshooting](#-troubleshooting) section
- Review the [FAQ](#-troubleshooting)
- Open an issue on GitHub

---

<div align="center">

**Made with ❤️ for the Bluetooth community**

**Part of the [Python Projects Collection](../README.md)**

</div>
