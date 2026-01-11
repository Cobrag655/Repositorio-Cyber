# CTF – DAV (Web)

## 🎯 Objetivo
Explorar uma aplicação web vulnerável para obter acesso inicial ao sistema e realizar escalada de privilégios até o usuário root.

---

## 🔎 Enumeração Inicial

Foi realizado um scan inicial de serviços para identificar possíveis vetores de ataque.

- O serviço **SSH não estava disponível**
- O serviço **Web estava ativo**

Com isso, toda a análise foi direcionada para ataques focados em aplicações web.

---

## 📂 Enumeração Web

Para mapear diretórios e recursos ocultos, foram utilizadas ferramentas de enumeração web:

- `gobuster`
- `dirb`

Através do **dirb**, foi identificado um diretório relacionado ao **WebDAV**, indicando que o servidor Apache possuía esse serviço habilitado.

Também foi utilizado:
- `wfuzz`, porém com uso limitado devido à falta de familiaridade no momento.

Mesmo assim, a enumeração foi suficiente para levantar a principal hipótese de ataque:
> WebDAV ativo com possível autenticação fraca.

---

## 🔐 Autenticação no WebDAV

Após identificar o serviço WebDAV, foi realizada uma pesquisa por **credenciais padrão** associadas a esse tipo de configuração.

Com isso, foi possível:
- Autenticar com sucesso no WebDAV
- Confirmar uma falha de configuração no serviço

---

## 🚀 Exploração – Acesso Inicial

Com acesso autenticado ao WebDAV, foi possível:

- Enviar arquivos ao servidor
- Executar um **reverse shell**

O shell reverso foi disparado utilizando `curl`, e a conexão foi recebida através do `netcat` na porta **1234**, garantindo acesso inicial ao sistema.

---

## 👤 Pós-Exploração – Usuário

Após obter acesso ao shell:

- Foi realizada a enumeração básica do sistema
- A flag **user.txt** foi localizada no diretório do usuário

---

## 🔑 Escalação de Privilégios

Para escalar privilégios, foi utilizado o comando:

- `sudo -l`

Foi identificado que o comando `cat` podia ser executado com **sudo sem necessidade de senha**.

Com isso, foi possível:
- Executar `cat` com privilégios de root
- Ler diretamente o arquivo `/root/root.txt`
- Obter a flag final

---

## 🧩 Solução (Visão Geral)

A solução do desafio baseou-se na identificação da ausência de serviços de acesso remoto tradicionais e na análise aprofundada do serviço web exposto.  
A enumeração revelou a presença de um WebDAV ativo, indicando uma configuração inadequada do servidor Apache.

O uso de credenciais padrão permitiu autenticação no serviço e o envio de arquivos ao servidor, resultando em acesso inicial via shell reverso.  
A escalada de privilégios foi alcançada devido a uma configuração insegura do `sudo`, que permitia a execução do comando `cat` com privilégios elevados sem autenticação, possibilitando a leitura direta da flag de root.

---

## 🛠️ Ferramentas Utilizadas
- nmap
- gobuster
- dirb
- wfuzz
- curl
- netcat

---

## 🧠 Aprendizados

Este CTF reforçou conceitos fundamentais, como:

- A importância da enumeração correta de serviços
- Como páginas web simples podem esconder serviços críticos
- WebDAV mal configurado representa um vetor real de ataque
- Credenciais padrão ainda são amplamente exploráveis
- Pequenas falhas em permissões de `sudo` podem levar ao comprometimento total do sistema

---

## 📌 Observação Final
Parte do desafio foi resolvida de forma independente.  
Em momentos específicos, write-ups foram utilizados como apoio para destravar o raciocínio e consolidar o aprendizado.

