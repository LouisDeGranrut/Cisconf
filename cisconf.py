# coding:utf-8
import argparse
import sys
import os

class couleurs:
    ROUGE = '\033[91m'
    VERT = '\033[92m'
    ORANGE = '\033[93m'
    BLUE = '\033[94m'
    FIN = '\033[0m'
    BOLD = '\033[1m'
    HEADER = '\033[95m'
    
def print_banner():
     
    print(couleurs.VERT + """ 
                _                                __                   _                        _   _             
  ___(_)___  ___ ___   ___ ___  _ __  / _|       __ _ _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __  
 / __| / __|/ __/ _ \ / __/ _ \| '_ \| |_ _____ / _` | | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
| (__| \__ \ (_| (_) | (_| (_) | | | |  _|_____| (_| | |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
 \___|_|___/\___\___/ \___\___/|_| |_|_|        \__,_|\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|
          
          """ + couleurs.FIN)   
    
def write_result_switch(nb_vlan,names_vlan,ips_vlan,hostname, password) :  
    print(couleurs.BLUE + "[+] Ecriture du resulat"+ couleurs.FIN)
    try : 
        f = open("configuration_" + hostname + ".txt", "a")
        f.write("en\n")
        f.write("conf t\n")
        f.write("hostname " + hostname + "\n")
        f.write("enable secret " + password + "\n")
        f.write("\n")
        for i in range(nb_vlan) :
            f.write("vlan " + str(i) + "\n") 
            f.write("name "+ names_vlan[i] + "\n")
            f.write("ip address " + ips_vlan[i] + "\n")
            f.close()
        print(couleurs.VERT + "[+] conf saved at : configuration_" + hostname + ".txt"+ couleurs.FIN)
    except :
        print(couleurs.ROUGE+"[-] Erreur d\'ecriture dans le fichier !"+couleurs.FIN)
        
def switch():
    try : 
        #variable
        ips_vlan = []
        names_vlan = []
        command = input("")
        #global configuration
        hostname = input("Enter switch name: ")
        password = input("Enter Enable password: ")
        
        print(couleurs.BLUE + "[*] For checking help on this module : type <help or h> "+ couleurs.FIN)
        
        if command == "help":
            print(couleurs.BLUE + "[*] {vlan, v}, {interface, int, i}, {interface range, ir}, {help, ?}, {end}"+ couleurs.FIN)
        else : 
            print(couleurs.BLUE + "[+] ==> VLAN CONFIGURATION" + couleurs.FIN)
            try :
                numb = int(input("Nombres d'interfaces VLAN : "))
                for i in range(numb):
                    names_vlan.append(input("[*] nom de l'interface " + str(i) + " :"))
                    ips_vlan.append(input("[*] addresse IP de l\'interface vlan " + str(i)+ " :"))
                    print("\n")
                write_result_switch(numb,names_vlan,ips_vlan,hostname,password)  
            except KeyboardInterrupt :
                print(couleurs.ORANGE +"\n[!] Interruption clavier"+ couleurs.FIN)
            except :
                print(couleurs.ROUGE +"[-] Ecrire un chiffre "+ couleurs.FIN)                  
    except KeyboardInterrupt :
        print(couleurs.ORANGE +"\n[!] Interruption clavier"+ couleurs.FIN)

def routeur():
    print(couleurs.ORANGE + "\n[!] Error : This mode must be configured later, Thank for your comprehension !" + couleurs.FIN)
    sys.exit(0)

if __name__ == '__main__':
    os.system('clear')
    print_banner()
    parser = argparse.ArgumentParser(description="Help to generate cisco configuration\n Degranrut Louis")
    parser.add_argument("-m", "--mode", dest="mode", help="choose switch (s) or router(r) configuration. Example : -m s")
    args = parser.parse_args()
    if args.mode == 's' :
        switch()
    elif args.mode == 'r': 
        routeur()
    else :
        print(couleurs.ROUGE + "[-] No mode provided !"+ couleurs.FIN)