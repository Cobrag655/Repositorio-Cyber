#importa tempo e processos do terminal
import time
import subprocess
import optparse
import os

def cons_arg():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface de rede")
    parser.add_option("-m", "--mac", dest="mac", help="Novo mac da interface")
    parser.add_option("-r", "--reset", dest="reset", help="Reseta o mac da interface escolhida")
    return parser.parse_args()

def get_mac_original(interface):
    #usa a ferramenta ethtool para buscar o mac original da placa
    try:
        out = subprocess.check_output(["ethtool", "-P", interface], text=True, stderr=subprocess.DEVNULL)
        # saída típica: "Permanent address: 12:34:56:78:9a:bc\n"
        for line in out.splitlines():
            line = line.strip()
            if line.lower().startswith("permanent address:"):
                return line.split(":", 1)[1].strip()
    except Exception:
        pass

def change_mac(reset, interface, mac):
    print("BEM VINDO AO MAC ADRESS CHANGE!!")

    if reset == "wlan0" or reset == "eth0":
        # • Busca o MAC original da interface
        mac_o = get_mac_original(reset)
        print(f"[+] Revertendo seu MAC {reset} para o original ({mac_o})")
        time.sleep(2)
        subprocess.call(f"sudo ifconfig {reset} down", shell=True)
        subprocess.call(f"sudo ifconfig {reset} hw ether {mac_o}", shell=True)
        subprocess.call(f"sudo ifconfig {reset} up", shell=True)
        print("[+] RESULTADO!!")
        subprocess.call("ifconfig | grep ether", shell=True)

    else:
        # • Salva o MAC original antes de mudar
        mac_original = get_mac_original(interface)
        if mac_original:
            with open(f"/tmp/mac_original_{interface}", "w") as f:
                f.write(mac_original)
        print(f"[+] Mudando seu mac {interface} para {mac}")
        time.sleep(2)
        subprocess.call(f"sudo ifconfig {interface} down", shell=True)
        subprocess.call(f"sudo ifconfig {interface} hw ether {mac}", shell=True)
        subprocess.call(f"sudo ifconfig {interface} up", shell=True)
        print("[+] RESULTADO!!")
        subprocess.call("ifconfig | grep ether", shell=True)

(options, arguments) = cons_arg()
change_mac(options.reset, options.interface, options.mac)
