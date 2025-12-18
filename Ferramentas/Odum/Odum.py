def reduz_ate_16(n):
    """Reduz número somando dígitos até <=16"""
    while n > 16:
        n = sum(int(d) for d in str(n))
    return n

def separa_digitos(data_str):
    """Extrai dígitos da data: "31/08/2008" -> [3,1,0,8,2,0,0,8]"""
    return [int(c) for c in data_str if c.isdigit()]

def calcula_vertical_e_colunas(digitos):
    """Calcula vertical (soma total) e colunas alternadas"""
    vertical = reduz_ate_16(sum(digitos))
    col1 = reduz_ate_16(sum(digitos[0::2]))  # posições 0,2,4,6
    col2 = reduz_ate_16(sum(digitos[1::2]))  # posições 1,3,5,7
    return vertical, col1, col2

def calcula_direita_esquerda_central(col1, col2):
    """Calcula P(esquerda), N(direita), central"""
    direita = reduz_ate_16(col1 + col2)           # N
    esquerda = reduz_ate_16(col1 + col2 + direita) # P
    central = reduz_ate_16(col1 + col2 + direita + esquerda)
    return direita, esquerda, central

def odum_prototipo(data_nascimento):
    """Calcula cruz para nascimento e 2026"""
    digitos_nasc = separa_digitos(data_nascimento)
    vert_nasc, col1_nasc, col2_nasc = calcula_vertical_e_colunas(digitos_nasc)
    dir_nasc, esq_nasc, cent_nasc = calcula_direita_esquerda_central(col1_nasc, col2_nasc)

    dia = data_nascimento[:2]
    mes = data_nascimento[3:5]
    data_2026 = f"{dia}/{mes}/2026"
    
    digitos_2026 = separa_digitos(data_2026)
    vert_2026, col1_2026, col2_2026 = calcula_vertical_e_colunas(digitos_2026)
    dir_2026, esq_2026, cent_2026 = calcula_direita_esquerda_central(col1_2026, col2_2026)

    return {
        "nasc_vertical": vert_nasc, "nasc_col1": col1_nasc, "nasc_col2": col2_nasc,
        "nasc_direita": dir_nasc, "nasc_esquerda": esq_nasc, "nasc_central": cent_nasc,
        "ano2026_vertical": vert_2026, "ano2026_col1": col1_2026, "ano2026_col2": col2_2026,
        "ano2026_direita": dir_2026, "ano2026_esquerda": esq_2026, "ano2026_central": cent_2026,
    }

def mostra_cruz(titulo, vertical, col1, col2, direita, esquerda, central):
    """Exibe cruz: CAB(col2), CAM(col1), N(direita), P(esquerda)"""
    print(f"\n=== {titulo} ===")
    print(f"odum: {vertical}")
    print()
    print(f"         CAB: {col2}")
    print(f"             |")
    print(f"    P: {esquerda} --- {central} --- N: {direita}")
    print(f"             |")
    print(f"         CAM: {col1}")

def mostra_resultados(resultados):
    # Nascimento
    mostra_cruz(
        "Nascimento",
        resultados["nasc_vertical"],
        resultados["nasc_col1"],
        resultados["nasc_col2"],
        resultados["nasc_direita"],
        resultados["nasc_esquerda"],
        resultados["nasc_central"]
    )
    
    # Ano 2026
    mostra_cruz(
        "Ano 2026",
        resultados["ano2026_vertical"],
        resultados["ano2026_col1"],
        resultados["ano2026_col2"],
        resultados["ano2026_direita"],
        resultados["ano2026_esquerda"],
        resultados["ano2026_central"]
    )

def main():
    data = input("Qual data de nascimento? (DD/MM/AAAA): ")
    mostra_resultados(odum_prototipo(data))

if __name__ == "__main__":
    main()
