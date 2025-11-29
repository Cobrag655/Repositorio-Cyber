# MAC Address Changer — Ferramenta Simples em Python

Este repositório contém uma ferramenta escrita em Python para **alterar** ou **resetar** o endereço MAC de uma interface de rede no Linux. Foi desenvolvida totalmente na raça, do zero, com foco em aprendizagem prática e no funcionamento real das interfaces de rede.

Ela utiliza comandos nativos como `ifconfig` e `ethtool`, além de operações básicas com arquivos e subprocessos do sistema.

---

## 🚀 Funcionalidades

✔️ Alterar o MAC de qualquer interface informada
✔️ Resetar a interface para o **MAC original** usando o `ethtool`
✔️ Salvar o MAC original em `/tmp` para futura restauração
✔️ Execução simples via linha de comando
✔️ Totalmente feita em Python puro, sem bibliotecas externas

---

## 🛠️ Como funciona internamente

A ferramenta:

1. Lê os argumentos passados pelo usuário usando `optparse`
2. Busca o MAC permanente utilizando `ethtool -P`
3. Usa comandos do sistema para desligar a interface, alterar o MAC e ligá‑la novamente
4. Exibe o resultado final usando `ifconfig | grep ether`

Tudo de forma direta, simples e funcional.

---

## 📦 Instalação

Clone o repositório:

```bash
git clone <link-do-seu-repositorio>
cd <nome-da-pasta>
```

Certifique-se de rodar com permissões elevadas:

```bash
sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

---

## 🧩 Uso

### ➤ Alterar o MAC

```bash
sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

### ➤ Resetar o MAC para o original

```bash
sudo python3 mac_changer.py -r wlan0
```

### ➤ Ver todas as opções

```bash
python3 mac_changer.py --help
```

---

## 📚 Exemplo de Saída

```
BEM VINDO AO MAC ADRESS CHANGE!!
[+] Mudando seu mac wlan0 para 00:11:22:33:44:55
[+] RESULTADO!!
[+] Seu mac atual é: 00:11:22:33:44:55
```

---

## ⚠️ Aviso Importante

👉 Alterar MAC Address pode desconectar sua rede ou causar instabilidade em algumas interfaces.
👉 Utilize com responsabilidade e **apenas em máquinas e redes que você tem autorização**.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais. Sinta‑se à vontade para modificar, estudar e melhorar.

---
