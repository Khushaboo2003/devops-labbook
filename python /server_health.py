import platform
import socket
import psutil

print("===== Server Health =====")

# Hostname
print("Hostname:", socket.gethostname())

# Operating System
print("OS:", platform.system(), platform.release())

# CPU Usage
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

# Memory Usage
memory = psutil.virtual_memory()
print("Memory Usage:", memory.percent, "%")

# Disk Usage
disk = psutil.disk_usage('/')
print("Disk Usage:", disk.percent, "%")

# Uptime
uptime = psutil.boot_time()
print("Boot Time:", uptime)

print("=========================")
