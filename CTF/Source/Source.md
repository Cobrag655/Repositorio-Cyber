# Source — TryHackMe

## 🧠 Descrição
CTF focado em enumeração de serviços e exploração de vulnerabilidade conhecida no Webmin.

## 🔍 Enumeração
Scan inicial realizado com Nmap:

nmap -sS --min-rate 5000 -p- --open -vvv -n -Pn <IP>

Porta suspeita identificada:
- 10000/tcp (HTTP)

## 🧪 Análise
O serviço na porta 10000 correspondia ao Webmin.
Enumeração web tradicional não apresentou resultados relevantes.

## 💥 Exploração
Vulnerabilidade explorada:
- Webmin `password_change.cgi` Backdoor
- CVE-2019-15107

Ferramenta utilizada:
- Metasploit (primeira experiência com a ferramenta)

Configurações principais:
- RHOSTS: IP do alvo
- LHOST: tun0
- SSL: true

## 🏴‍☠️ Resultado
- Acesso remoto obtido com sucesso
- Shell com privilégios de root
- Flags `user.txt` e `root.txt` localizadas

## ✅ Status
CTF concluído com sucesso.

