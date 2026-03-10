import re

def analise_de_senhas(senhas):
    
    testes = {
        "tamanho minimo (8')": r".{8,}", 
        "letras minusculas":   r"[a-z]",
        "letras maiusculas":   r"[A-Z]",
        "numeros": r"\d",
        "simbolos (!@#$%&)": r"[!@#$%&]" 
    }

    relatorio = {nome: bool(re.search(padrao, senhas)) for nome, padrao in testes.items()}

    pontuacao = sum(relatorio.values())

    niveis = ["muito fraca 🔴", "fraca 🟠 ", "media 🟡", "forte 🟢", "muito forte🔵"]

    
    classificacao = niveis[min(pontuacao, len(niveis)-1)]

    return relatorio, classificacao