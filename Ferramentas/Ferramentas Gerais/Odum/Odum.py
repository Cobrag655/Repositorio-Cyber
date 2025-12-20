def reduz_ate_16(n):
    """Reduz número somando dígitos até ficar <= 16."""
    while n > 16:
        n = sum(int(d) for d in str(n))
    return n


def separa_digitos(data_str):
    """Extrai apenas os dígitos da string de data."""
    return [int(c) for c in data_str if c.isdigit()]


def calcula_cruz(digitos):
    """Lógica RIGOROSA da cruz."""
    # odum principal (vertical)
    soma_total = sum(digitos)
    odum = reduz_ate_16(soma_total)

    # a = soma das posições 1,3,5,7 (índices 0,2,4,6)
    soma_a = digitos[0] + digitos[2] + digitos[4] + digitos[6]
    a = reduz_ate_16(soma_a)

    # b = soma das posições 2,4,6,8 (índices 1,3,5,7)
    soma_b = digitos[1] + digitos[3] + digitos[5] + digitos[7]
    b = reduz_ate_16(soma_b)

    # c, d, e
    c = reduz_ate_16(a + b)
    d = reduz_ate_16(a + b + c)
    e = reduz_ate_16(a + b + c + d)

    return odum, a, b, c, d, e


def odum_prototipo(data_nascimento):
    """Calcula APENAS nascimento (2026 cortado por manutenção)."""
    digitos_nasc = separa_digitos(data_nascimento)
    odum, a, b, c, d, e = calcula_cruz(digitos_nasc)

    return {
        "nasc_vertical": odum,
        "nasc_col1": a,      # CAM (baixo)
        "nasc_col2": b,      # CAB (cima)
        "nasc_direita": c,
        "nasc_esquerda": d,
        "nasc_central": e,
        # 2026 CORTADO POR MANUTENÇÃO
    }


def mostra_cruz(titulo, vertical, col1, col2, direita, esquerda, central):
    print(f"\n=== {titulo} ===")
    print(f"odum: {vertical}")
    print()
    print(f"         CAB: {col2}")
    print(f"             |")
    print(f"    P: {esquerda} --- {central} --- N: {direita}")
    print(f"             |")
    print(f"         CAM: {col1}")


def main():
    data = input("Qual data de nascimento? (DD/MM/AAAA): ")
    resultados = odum_prototipo(data)
    mostra_cruz(
        "Nascimento",
        resultados["nasc_vertical"],
        resultados["nasc_col1"],
        resultados["nasc_col2"],
        resultados["nasc_direita"],
        resultados["nasc_esquerda"],
        resultados["nasc_central"]
    )
    print("\n[2026 CORTADO POR MANUTENÇÃO DURANTE TEMPO INDETERMINADO]")


if __name__ == "__main__":
    main()
