# Adiciona compatibilidade com python 2 e 3
from __future__ import print_function
# Importa tempo e processos do terminal
import time
import subprocess
import optparse
import re


# Adiciona as funçoes em formato de ferramenta do linux
def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface de rede")
    parser.add_option("-m", "--mac", dest="mac", help="Novo mac da interface")
    parser.add_option("-r", "--reset", dest="reset", help="Reseta o mac da interface escolhida")
    return parser.parse_args()


def get_mac_original(interface):
    # Usa a ferramenta ethtool para buscar o mac original da placa
    try:
        out = subprocess.check_output(
            ["ethtool", "-P", interface],
            universal_newlines=True,
            stderr=subprocess.DEVNULL
        )
        # saída típica: "Permanent address: 12:34:56:78:9a:bc\n"
        for line in out.splitlines():
            line = line.strip()
            if line.lower().startswith("permanent address"):
                return line.split(":", 1)[1].strip()
    except Exception:
        pass


def mostrar_mac_atual(interface):
    # Função que mostra o MAC atual usando regex
    try:
        # Corrigido: concatenação correta pro Python 2/3
        comando = "ifconfig " + interface
        resultado_ifconfig = subprocess.check_output(
            comando, shell=True, universal_newlines=True
        )

        # Regex para buscar o padrão XX:XX:XX:XX:XX:XX
        mac_atual = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(resultado_ifconfig))

        # Se o MAC for encontrado, printa ele, senão avisa que não foi possível obter
        if mac_atual:
            print("[+] Seu MAC atual é: {}".format(mac_atual.group(0)))
        else:
            print("[-] Não foi possível obter o MAC atual.")

    except subprocess.CalledProcessError:
        print("[-] Erro ao executar ifconfig para essa interface.\n")


def change_mac(reset, interface, mac):
    print("BEM VINDO AO MAC ADRESS CHANGE!!")

    if reset:
        # Busca o MAC original da interface
        interface = reset
        mac_o = get_mac_original(interface)

        # Printa a ação de reset
        print("[+] Revertendo seu MAC {} para o original ({})".format(interface, mac_o))
        time.sleep(2)

        # Corrigido: faltavam operadores de concatenação "+"
        subprocess.call("sudo ifconfig " + interface + " down", shell=True)
        subprocess.call("sudo ifconfig " + interface + " hw ether " + mac_o, shell=True)
        subprocess.call("sudo ifconfig " + interface + " up", shell=True)
        
        # Printa o resultado
        print("[+] RESULTADO!!")
        mostrar_mac_atual(interface)

    else:
        # Salva o MAC original antes de mudar
        mac_original = get_mac_original(interface)
        if mac_original:
            caminho = "/tmp/mac_original_{}".format(interface)
            with open(caminho, "w") as f:
                f.write(mac_original)

        print("[+] Mudando seu mac {} para {}".format(interface, mac))
        time.sleep(2)

        # Corrigido: faltavam operadores de concatenação "+"
        subprocess.call("sudo ifconfig " + interface + " down", shell=True)
        subprocess.call("sudo ifconfig " + interface + " hw ether " + mac, shell=True)
        subprocess.call("sudo ifconfig " + interface + " up", shell=True)

        # Printa o resultado
        print("[+] RESULTADO!!")
        mostrar_mac_atual(interface)


# Executa o codigo
(options, args) = get_arguments()
change_mac(options.reset, options.interface, options.mac)
