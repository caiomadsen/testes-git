"""Primeiro script da jornada: saudação e catálogo de produtos."""

SAUDACAO = "=== Hello, World! Bem-vindo à Jornada de Dados ==="

PRODUTOS = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor",
    "Headset",
    "Webcam",
    "Impressora",
    "Cadeira Gamer",
    "SSD 1TB",
    "Hub USB-C",
]


def main():
    print(SAUDACAO)
    print()
    print(f"Catálogo com {len(PRODUTOS)} produtos:")

    for posicao, produto in enumerate(PRODUTOS, start=1):
        print(f"{posicao:>2}. {produto}")


if __name__ == "__main__":
    main()
