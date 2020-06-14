#!/usr/env python
import platform
# Architecture
print("Architecture info: " + platform.architecture()[0])
# machine
print("Machine info: " + platform.machine())
# node
print("Node info: " + platform.node())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution info: " + dist)

# processor
print("Processors info: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)


 
# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# Load
Print(“Load info:”)
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())

#disk usage
Print(“disk usage info:”
Threshold = 10
Child = subprocess.poppen([‘df’, ‘-h’], stdout=subprocess.PIPE)
Output = child.communicate()[0].strip().split(“/n”) 
For x in output[1:0]:
     If int(x.split()[-2][:-1]) >= threshold:
	 Print x 
# network info
def all_interfaces():
    max_possible = 128  # arbitrary. raise if needed.
    bytes = max_possible * 32
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * bytes)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        s.fileno(),
        0x8912,  # SIOCGIFCONF
        struct.pack('iL', bytes, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    lst = []
    for i in range(0, outbytes, 40):
        name = namestr[i:i+16].split('\0', 1)[0]
        ip   = namestr[i+20:i+24]
        lst.append((name, ip))
    return lst

def format_ip(addr):
    return str(ord(addr[0])) + '.' + \
           str(ord(addr[1])) + '.' + \
           str(ord(addr[2])) + '.' + \
           str(ord(addr[3]))


ifs = all_interfaces()
for i in ifs:
    print "%12s   %s" % (i[0], format_ip(i[1]))
