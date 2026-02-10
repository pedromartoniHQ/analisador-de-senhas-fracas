from checker import verificar_senha, classificar_senha

def main():
    print("=== Verificador de Força de Senha ===")
    senha = input("Digite a senha para análise: ")

    criterios = verificar_senha(senha)
    classificacao = classificar_senha(criterios)

    print("\nResultado:")
    for criterio, status in criterios.items():
        print(f"- {criterio.replace('_', ' ').title()}: {'OK' if status else 'FALHOU'}")

    print(f"\nClassificação final da senha: {classificacao}")


if __name__ == "__main__":
    main()