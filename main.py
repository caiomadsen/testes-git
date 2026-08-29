"""Primeiro script da jornada: saudação e catálogo de produtos."""

SAUDACAO = "=== Hello, World! Bem-vindo à Jornada de Dados ==="

CANAL_DESCRICOES = {
    "canal 1": "Hardware e Periféricos",
    "canal 2": "Jogos do Ano",
    "canal 3": "Softwares Gráficos e Sistemas Operacionais",
}

PRODUTOS = {
    "canal 1": [
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
    ],
    "canal 2": [
        "Baldur's Gate 3",
        "Elden Ring",
        "Cyberpunk 2077: Phantom Liberty",
        "Hogwarts Legacy",
        "Alan Wake 2",
        "Starfield",
        "Diablo IV",
        "Resident Evil 4 Remake",
        "Spider-Man 2",
        "Zelda: Tears of the Kingdom",
    ],
    "canal 3": [
        "Adobe Photoshop",
        "Adobe Illustrator",
        "Adobe Premiere Pro",
        "Figma",
        "CorelDRAW",
        "Blender",
        "AutoCAD",
        "Windows 11 Pro",
        "macOS Sonoma",
        "Ubuntu 24.04 LTS",
    ],
}


def main():
    print(SAUDACAO)
    print()

    for canal, produtos in PRODUTOS.items():
        descricao = CANAL_DESCRICOES[canal]
        print(f"Catálogo '{descricao}' com {len(produtos)} produtos:")
        for posicao, produto in enumerate(produtos, start=1):
            print(f"{posicao:>2}. {produto}")
        print()


if __name__ == "__main__":
    main()
