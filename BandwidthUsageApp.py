import psutil
import time
import os
import ctypes
from collections import defaultdict

# To store the starting values so we can show "Total Session Consumption"
start_stats = {}

def is_admin():
    """Checks if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        # For Non-Windows systems
        return os.getuid() == 0

def get_process_network_usage():
    current_usage = []
    
    # Iterate through all connections to find active 'talkers'
    # kind='inet' includes both IPv4 and IPv6
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.pid:
            try:
                p = psutil.Process(conn.pid)
                p_name = p.name()
                
                # Get I/O counters (Read = Incoming, Write = Outgoing)
                io = p.io_counters()
                
                # Baseline tracking
                if conn.pid not in start_stats:
                    start_stats[conn.pid] = {'read': io.read_bytes, 'write': io.write_bytes}
                
                # Delta calculation (MB)
                consumed_recv = (io.read_bytes - start_stats[conn.pid]['read']) / (1024**2)
                consumed_sent = (io.write_bytes - start_stats[conn.pid]['write']) / (1024**2)
                
                current_usage.append({
                    'pid': conn.pid,
                    'name': p_name,
                    'sent': consumed_sent,
                    'recv': consumed_recv
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    unique_usage = {v['pid']: v for v in current_usage}.values()
    return sorted(unique_usage, key=lambda x: x['recv'], reverse=True)

def main():
    # --- ADMIN CHECK ---
    admin_status = is_admin()
    print("--- Security Check ---")
    if admin_status:
        print("[OK] Running with Administrator privileges.")
    else:
        print("[WARNING] Not running as Administrator.")
        print("Some processes and network data may be hidden or inaccessible.")
    
    choice = input("\nWould you like to start monitoring? (y/n): ").lower()
    if choice != 'y':
        print("Exiting...")
        return

    print("\nInitializing Application-Level Tracker...")
    time.sleep(1)

    try:
        while True:
            process_list = get_process_network_usage()
            
            os.system('cls' if os.name == 'nt' else 'clear')
            #Create titles/headings
            print("--- Network Bandwidth Monitor ---")
            print("Press Ctrl+C to stop monitoring.\n")
            
            # Create a table to display results
            print(f"{'PID':<8} | {'Application':<25} | {'Sent (MB)':<12} | {'Received (MB)':<12}")
            print("-" * 65)
            
            for proc in process_list:
                if proc['sent'] > 0.01 or proc['recv'] > 0.01:
                    print(f"{proc['pid']:<8} | {proc['name']:<25} | {proc['sent']:<12.2f} | {proc['recv']:<12.2f}")
            
            if not process_list:
                print("\nNo active network applications detected...")
                
            time.sleep(1) # Refresh rate set to 1 second
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()