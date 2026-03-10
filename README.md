<<<<<<< HEAD
#análise de senhas fracas
Nesta atualização, o código deixou de ser uma sequência de ifs repetitivos e passou a usar uma lógica mais profissional.
Em vez de verificar cada critério manualmente, agora usei  um dicionário de Expressões Regulares (Regex) que estou aprendendo na faculdade. Isso permite que o código "percorra" as regras sozinho.
Melhorei a interface do terminal com emojis e um sistema de cores (🔴, 🟠, 🟡, 🟢, 🔵) para facilitar a leitura para os usuarios.
 
 #Critérios de Segurança
 Comprimento: Pelo menos 8 caracteres (o padrão ouro da web).
Diversidade: Uso obrigatório de maiúsculas, minúsculas, números e símbolos.
=======
# verificação de senhas fracas🔐
>>>>>>> 6b1a822623168357192001e7cf074ffdcd56056e

#FERRAMENTAS UTILIZADAS
PYTHON  3.13.7
BIBLIOTECA re
#como rodar o projeto
verifica-se de ter o python  3.13.7
 Você pode verificar digitando no seu terminal ou CMD:python --v
Copie o código do script.
Crie um novo arquivo na sua pasta de preferência e nomeie-o como analise_de_senhas.py.
Cole o código dentro desse arquivo e salve.
Após rodar o comando, o programa pedirá que você digite uma senha:
Digite a senha que deseja testar.
Aperte Enter.
O sistema exibirá o relatório de quais critérios você atingiu e o status final de segurança.
