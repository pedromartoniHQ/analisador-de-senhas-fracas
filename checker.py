import re

def verificar_senha(senha: str) -> dict:
    criterios = {
        "tamanho_minimo": len(senha) >= 8,
        "minuscula": bool(re.search(r"[a-z]", senha)),
        "maiuscula": bool(re.search(r"[A-Z]", senha)),
        "numero": bool(re.search(r"\d", senha)),
        "especial": bool(re.search(r"[!@#$%&*]", senha))
    }
    return criterios


def classificar_senha(criterios: dict) -> str:
    pontos = sum(criterios.values())

    if pontos <= 2:
        return "FRACA"
    elif pontos <= 4:
        return "MÉDIA"
    else:
        return "FORTE"