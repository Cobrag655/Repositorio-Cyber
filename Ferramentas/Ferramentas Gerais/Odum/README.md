Odum Cruz Numerológica

Calculadora numerológica que gera a "Cruz Odum" a partir da data de nascimento.
✨ O que faz?

Para qualquer data DD/MM/AAAA calcula:

    Cruz do Nascimento (odum + CAB/CAM/P/N)

    Cruz Ano 2026 (mesmo dia/mês no futuro)

text
         CAB
            |
   P --- CENTRO --- N
            |
         CAM

📱 Como usar no CELULAR
Termux (Android)

bash
pkg update && pkg install python
nano odum.py  # Cole o código
python odum.py

Pydroid 3 (Android)

    Baixe na Play Store

    Cole código → ▶️ Executar

🚀 Exemplo de Saída

text
=== Nascimento ===
odum: 10

         CAB: 12
             |
    P: 8 --- 7 --- N: 5
             |
         CAM: 11

💻 Executar no PC

bash
python odum.py

📝 Como funciona

    Extrai dígitos: 31/08/2008 → [3,1,0,8,2,0,0,8]

    Reduz até ≤16: soma dígitos repetidamente

    Colunas:

        CAM = soma posições 0,2,4,6

        CAB = soma posições 1,3,5,7

    Cruz: P/N/Centro derivados das colunas

🔧 Funções
Função	Descrição
reduz_ate_16(n)	Reduz soma até ≤16
separa_digitos()	Extrai dígitos da data
calcula_vertical_e_colunas()	Calcula odum + CAM/CAB
calcula_direita_esquerda_central()	Calcula P/N/Centro
odum_prototipo()	Gera cruz nascimento + 2026
📂 Estrutura

text
Odum.py          # Código principal
README.md         # Este arquivo

⚙️ Dependências

text
Python 3.6+
Nenhuma biblioteca externa!

🔮 Teste sua data

text
$ python odum.py
Qual data de nascimento? (DD/MM/AAAA): 15/07/1995
[Mostra as duas cruzes]

📄 Licença

MIT License - Use livremente! ✨

Feito com ❤️ para numerologia brasileira 😎
