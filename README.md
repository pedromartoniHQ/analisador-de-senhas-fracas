# 🛡️ Verificador de Senhas Pro: Versão 2.0

Olá! Este é o meu projeto de **Análise de Segurança de Senhas**. Ele nasceu como um script simples e evoluiu para uma ferramenta modular, limpa e inteligente, focada em ajudar usuários a criarem senhas que realmente protejam seus dados.

## 🚀 Por que este projeto é especial?

Diferente de validadores básicos, esta versão 2.0 foi totalmente **refatorada**. Isso significa que o código foi "limpo" para seguir as melhores práticas de mercado:

*   **Modularização:** O projeto é dividido em peças. Temos a "inteligência" (lógica) em um arquivo e a "interface" (conversa com o usuário) em outro.
*   **Padrões de Busca (Regex):** Utilizamos expressões regulares profissionais para identificar letras, números e símbolos com precisão.
*   **Código "Pythonico":** Menos repetição, mais eficiência. Usamos lógica de soma de booleanos para classificar a força da senha de 0 a 5.

---

## 📂 Estrutura do Projeto

Para manter tudo organizado, o projeto conta com dois arquivos principais:

1.  **`analise_de_senhas.py`**: O coração do projeto. Contém todas as regras matemáticas e os filtros de segurança.
2.  **`main.py`**: A porta de entrada. É o arquivo que você executa para interagir com o programa.

---

## 🛠️ Como Rodar na Sua Máquina

Se você quiser testar o projeto no seu computador, siga estes passos simples:

### 1. Pré-requisitos
Você só precisa do **Python 3** instalado. Para conferir se já tem, digite no terminal:
```bash
python --version

