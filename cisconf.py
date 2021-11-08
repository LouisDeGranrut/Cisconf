print("=====CISCO CONFIG EDITOR=====")
print("Welcome to Cisconf")
print("The Cisco configuration file creator")
print("by Louis de Granrut")
print("=============================")

print("Create config file for:")
print("1 - Switch")
print("2 - Router")

answer = input("")
if(answer == "Switch" or answer == "switch" or answer == "s"):
    print("Switch")
else :
    print("Router")

#-------------------------------------------------------------------------------------------------------
hostname = input("Enter machine name: ")
password = input("Enter Enable password: ")


#configure interface (switchport, ip add, no shut)
#ospf
#ip routing
#dhcp

f = open("configuration.txt", "a")
f.write("en\n")
f.write("conf t\n")
f.write("hostname " + hostname + "\n")
f.write("enable secret " + password + "\n")

command = input("")

while(command != "end"):
    
    #vlan-----------------------------------------------------------------------------------------------
    if (command == "vlan" or command == "v"):
        numb = input("Vlan number: ")
        ipadd = input("Vlan address: ")
        f.write("vlan " + numb + "\n interface vlan " + numb + "\n ip add " + ipadd + "\n ex \n")
        command = input("")

    #interface------------------------------------------------------------------------------------------
    if (command == "interface" or command == "int" or command == "i"):
        intname = input("Interface Name: ")
        ipadd = input("Interface address: ")
        #encapsulation dot1Q
        switchport = input("Switchport mode: ")
        f.write("interface " + intname + "\n ip add " + ipadd + "\n" + switchport+ "\n no shut\n ex \n")
        command = input("")
    #interface range------------------------------------------------------------------------------------------
    if (command == "interface range" or command == "ir"):
        intname = input("Interface Name: ")
        to = input("To: ")
        #spanning tree
        channelgroup = input("Channel Group number: ")
        channelgroupMode = input("Channel Group Mode (auto, desirable, on, active, passive): ")
        f.write("interface range " + intname + "-" + to + "\n channel-group " + channelgroup + " mode " + channelgroupMode + "\n")
        command = input("")
    #....
    if(command == ""):
       command = input("")

f.write("wr\n")
f.close()
print("Config file created !")


