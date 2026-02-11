TryHackMe: Billing

🧠 Resumo do CTF

Objetivo: Enumerar → Shell via CVE-2023-30258 → Root via Fail2ban sudo abuse.

text
nmap → MagnusBilling v3 → MSF RCE (asterisk) → sudo fail2ban-client → SUID bash → root.txt

📋 Passos principais

    Nmap agressivo revelou portas 22/80/3306/5060/8088

    WFuzz/SQLMap travados pelo Fail2ban (ban IP)

    MSFConsole → CVE-2023-30258 → reverse shell asterisk

    Pseudo-TTY + sudo -l → fail2ban-client root sem senha

    Fail2ban privesc: configs custom /tmp/ → action maliciosa → bash SUID

    /tmp/bash -p → root.txt

💡 Destaque técnico

Fail2ban irony: ferramenta anti-ataque virou vetor de privesc. Reverse shell sobreviveu ao ban IP.

Tempo: ~1h | Dificuldade: Facíl

obs: ocorreu um problema e por conta disso não consegui colocar os prints necessarios sobre o teste.
