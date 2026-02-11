TryHackMe: Blue

Room iniciante do TryHackMe que ensina vulnerabilidades SMB do Windows usando EternalBlue (MS17-010). Perfeita pra quem tá começando com Metasploit e cracking de hashes.
Fluxo básico

    Nmap acha SMB (porta 445) aberta

    Metasploit com ms17_010_eternalblue gera shell

    Upgrade pra Meterpreter (sessions -u 1)

    Hashdump pega hashes LM/NT dos usuários

    John quebra senha do "Jon" (rockyou.txt)

    Login com credenciais novas nos shares

    Flags nos desktops clássicos

Pontos importantes

    Senha do Jon: fruity

    LM hash vazio (senha em branco comum)

    NT é o hash real pra crackear

    Flags: harvey/Documents, Jon/Desktop, Administrator/Desktop

Tempo: 1h | Dificuldade: Fácil | Skills: Nmap + Metasploit + John

Ideal pra praticar enumeração Windows e primeiro exploit real!
