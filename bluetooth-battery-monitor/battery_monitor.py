"""
Bluetooth Headset Battery Indicator
====================================
Check battery percentage of Bluetooth devices connected to Windows PC

Supports multiple methods:
1. Windows Bluetooth API (via bleak)
2. PowerShell integration
3. WMI queries

Requirements:
    pip install bleak psutil wmi

Author: Python Projects Collection
"""

import asyncio
import subprocess
import sys
from datetime import datetime

# Try importing optional libraries
try:
    from bleak import BleakScanner, BleakClient
    BLEAK_AVAILABLE = True
except ImportError:
    BLEAK_AVAILABLE = False
    print("⚠️  'bleak' not installed. Install with: pip install bleak")

try:
    import wmi
    WMI_AVAILABLE = True
except ImportError:
    WMI_AVAILABLE = False
    print("⚠️  'wmi' not installed. Install with: pip install wmi")


class BluetoothBatteryChecker:
    """Check battery levels of Bluetooth devices"""
    
    def __init__(self):
        self.devices = []
    
    async def scan_bluetooth_devices(self):
        """Scan for nearby Bluetooth devices using BLE"""
        if not BLEAK_AVAILABLE:
            print("❌ Bleak library not available")
            return []
        
        print("🔍 Scanning for Bluetooth devices...")
        devices = await BleakScanner.discover(timeout=10.0)
        
        self.devices = []
        for device in devices:
            info = {
                'name': device.name or 'Unknown',
                'address': device.address,
                'rssi': device.rssi
            }
            self.devices.append(info)
            print(f"  📱 Found: {info['name']} ({info['address']})")
        
        return self.devices
    
    async def get_battery_level_ble(self, address):
        """
        Get battery level using BLE (Bluetooth Low Energy)
        Battery Service UUID: 0000180f-0000-1000-8000-00805f9b34fb
        Battery Level Characteristic: 00002a19-0000-1000-8000-00805f9b34fb
        """
        if not BLEAK_AVAILABLE:
            return None
        
        try:
            print(f"🔌 Connecting to {address}...")
            async with BleakClient(address, timeout=15.0) as client:
                if not client.is_connected:
                    print("❌ Failed to connect")
                    return None
                
                print("✅ Connected!")
                
                # Battery Service UUID
                BATTERY_SERVICE_UUID = "0000180f-0000-1000-8000-00805f9b34fb"
                BATTERY_LEVEL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
                
                # Try to read battery level
                try:
                    battery_level = await client.read_gatt_char(BATTERY_LEVEL_UUID)
                    battery_percentage = int(battery_level[0])
                    return battery_percentage
                except Exception as e:
                    print(f"⚠️  Battery service not available: {e}")
                    return None
                    
        except Exception as e:
            print(f"❌ Error connecting: {e}")
            return None
    
    def get_battery_powershell(self):
        """Get Bluetooth device battery using PowerShell"""
        try:
            # PowerShell command to get Bluetooth devices
            ps_command = """
            Get-PnpDevice -Class Bluetooth | Where-Object {$_.Status -eq 'OK'} | 
            ForEach-Object {
                $device = $_
                $battery = Get-PnpDeviceProperty -InstanceId $device.InstanceId -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' -ErrorAction SilentlyContinue
                if ($battery) {
                    [PSCustomObject]@{
                        Name = $device.FriendlyName
                        Status = $device.Status
                        Battery = $battery.Data
                    }
                }
            } | ConvertTo-Json
            """
            
            result = subprocess.run(
                ["powershell", "-Command", ps_command],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0 and result.stdout.strip():
                print("📊 PowerShell Results:")
                print(result.stdout)
                return result.stdout
            else:
                print("⚠️  No battery info available via PowerShell")
                return None
                
        except Exception as e:
            print(f"❌ PowerShell error: {e}")
            return None
    
    def get_battery_wmi(self):
        """Get battery information using WMI (Windows Management Instrumentation)"""
        if not WMI_AVAILABLE:
            print("❌ WMI library not available")
            return None
        
        try:
            print("🔍 Checking WMI for Bluetooth devices...")
            c = wmi.WMI()
            
            # Query for Bluetooth devices
            devices = c.Win32_PnPEntity(ConfigManagerErrorCode=0)
            bluetooth_devices = []
            
            for device in devices:
                if device.Name and 'bluetooth' in device.Name.lower():
                    bluetooth_devices.append({
                        'name': device.Name,
                        'device_id': device.DeviceID,
                        'status': device.Status
                    })
            
            if bluetooth_devices:
                print(f"📱 Found {len(bluetooth_devices)} Bluetooth devices:")
                for dev in bluetooth_devices:
                    print(f"  • {dev['name']}")
                return bluetooth_devices
            else:
                print("⚠️  No Bluetooth devices found via WMI")
                return None
                
        except Exception as e:
            print(f"❌ WMI error: {e}")
            return None
    
    def get_battery_windows_api(self):
        """
        Get battery using Windows Bluetooth API
        Note: Requires specific Windows 10/11 Bluetooth capabilities
        """
        try:
            # Try using Windows Runtime APIs (requires Windows 10+)
            ps_command = """
            $devices = Get-PnpDevice | Where-Object {$_.Class -eq 'Bluetooth' -and $_.Status -eq 'OK'}
            foreach ($device in $devices) {
                Write-Host "Device: $($device.FriendlyName)"
                Write-Host "Status: $($device.Status)"
                Write-Host "---"
            }
            """
            
            result = subprocess.run(
                ["powershell", "-Command", ps_command],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                return result.stdout
            return None
            
        except Exception as e:
            print(f"❌ Windows API error: {e}")
            return None


def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print("🎧 BLUETOOTH HEADSET BATTERY CHECKER 🔋")
    print("="*60)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


def print_menu():
    """Print menu options"""
    print("\n📋 Select Method:\n")
    print("1. 🔍 Scan for BLE devices and check battery")
    print("2. 💻 Use PowerShell to check battery")
    print("3. 🖥️  Use WMI to list Bluetooth devices")
    print("4. 🪟 Use Windows API")
    print("5. 🔄 Try all methods")
    print("6. ❌ Exit")
    print()


async def main():
    """Main application function"""
    print_header()
    
    # Check available libraries
    print("📦 Checking dependencies...")
    print(f"  • Bleak (BLE): {'✅ Available' if BLEAK_AVAILABLE else '❌ Not installed'}")
    print(f"  • WMI: {'✅ Available' if WMI_AVAILABLE else '❌ Not installed'}")
    print()
    
    if not BLEAK_AVAILABLE and not WMI_AVAILABLE:
        print("⚠️  No Bluetooth libraries available!")
        print("📥 Install with: pip install bleak wmi")
        print()
    
    checker = BluetoothBatteryChecker()
    
    while True:
        print_menu()
        choice = input("👉 Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # BLE Scan method
            if not BLEAK_AVAILABLE:
                print("❌ Bleak not installed. Install with: pip install bleak")
                continue
            
            print("\n" + "─"*60)
            devices = await checker.scan_bluetooth_devices()
            
            if devices:
                print(f"\n✅ Found {len(devices)} device(s)")
                print("\nSelect a device to check battery:")
                for i, dev in enumerate(devices, 1):
                    print(f"  {i}. {dev['name']} ({dev['address']})")
                
                try:
                    dev_choice = int(input("\n👉 Enter device number: ")) - 1
                    if 0 <= dev_choice < len(devices):
                        device = devices[dev_choice]
                        print(f"\n🔋 Checking battery for: {device['name']}")
                        battery = await checker.get_battery_level_ble(device['address'])
                        
                        if battery is not None:
                            print(f"\n{'─'*40}")
                            print(f"🎧 Device: {device['name']}")
                            print(f"🔋 Battery: {battery}%")
                            print(f"{'─'*40}\n")
                        else:
                            print("⚠️  Could not read battery level")
                            print("💡 Note: Device must support Battery Service")
                    else:
                        print("❌ Invalid device number")
                except ValueError:
                    print("❌ Invalid input")
            else:
                print("⚠️  No devices found")
        
        elif choice == '2':
            # PowerShell method
            print("\n" + "─"*60)
            checker.get_battery_powershell()
        
        elif choice == '3':
            # WMI method
            print("\n" + "─"*60)
            checker.get_battery_wmi()
        
        elif choice == '4':
            # Windows API method
            print("\n" + "─"*60)
            result = checker.get_battery_windows_api()
            if result:
                print(result)
        
        elif choice == '5':
            # Try all methods
            print("\n" + "="*60)
            print("🔄 TRYING ALL METHODS")
            print("="*60)
            
            print("\n1️⃣  METHOD 1: BLE Scan")
            print("─"*60)
            if BLEAK_AVAILABLE:
                await checker.scan_bluetooth_devices()
            else:
                print("❌ Bleak not available")
            
            print("\n2️⃣  METHOD 2: PowerShell")
            print("─"*60)
            checker.get_battery_powershell()
            
            print("\n3️⃣  METHOD 3: WMI")
            print("─"*60)
            checker.get_battery_wmi()
            
            print("\n4️⃣  METHOD 4: Windows API")
            print("─"*60)
            checker.get_battery_windows_api()
        
        elif choice == '6':
            print("\n👋 Goodbye!\n")
            break
        
        else:
            print("❌ Invalid choice. Please select 1-6.")
        
        input("\n⏸️  Press Enter to continue...")
        print("\n" * 2)


def install_dependencies():
    """Helper function to install required dependencies"""
    print("📥 Installing required dependencies...\n")
    packages = ['bleak', 'wmi', 'psutil']
    
    for package in packages:
        print(f"Installing {package}...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', package])
    
    print("\n✅ Installation complete!")


if __name__ == "__main__":
    # Check if user wants to install dependencies
    if len(sys.argv) > 1 and sys.argv[1] == '--install':
        install_dependencies()
    else:
        try:
            # Run the async main function
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user. Goodbye!\n")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("💡 Try running: python batteryindicatorheadset.py --install")
