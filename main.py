from analise_de_senhas import analise_de_senhas

def main():
    print("----check-up de segurança ---")
    senha = input("digite a sua senha: ").strip()
    
    if not senha:
        print("senha vazia")
        return
    
    check, nivel = analise_de_senhas(senha)

    print("\ncomo foi seu desempenho:")
    for item, passou in check.items():
        icone = "✅" if passou else "❌"
        print(f"{icone} {item}")

    print(f"\nstatus final : {nivel}")


if __name__ == "__main__":
    main()


    
