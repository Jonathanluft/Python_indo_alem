# FIAP - Inteligência artificial e data science

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Cap 6 - Python e além

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Guilherme Campos Hermanowski </a>
- <a href="https://www.linkedin.com/company/inova-fusca">ana carolina belchior </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Bruno Gambarini </a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Matheus Soares Bento da Silva </a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jonathan Willian Luft </a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


## 📜 Descrição

A solução busca controlar o estoque de 3 culturas produzidas, quando abaixo do nível mínimo aceitável exibe um alerta.

além disso salva todos os registros em um arquivo json e adiciona as informações em uma banco de dados usando SQL.

SUBALGORITMOS:

ler_json()

Verifica existência do arquivo: Se não existe → Retorna []. Se existe → Abre o arquivo e lê seu conteúdo. Converte o JSON para uma estrutura Python (lista de dicionários). Retorna a estrutura (lista de dicionários).

salvar_json()

Abre o arquivo em modo de escrita (cria se não existir). Converte a lista de dicionários para JSON com formatação amigável. Salva os dados no arquivo e fecha automaticamente

inserir Oracle()

Tenta conectar ao Oracle e inserir o registro. Se ocorrer erro Exibe detalhes do erro. Se tudo der certo Os dados são salvos na tabela COLHEITAS.

validar_float()

Recebe uma string Faz um loop infinito e entra em um try Recebe o valor do user e tenta converter pra float Caso não consiga exibe "Digite número válido!"

validar tipo()

Basicamente a mesma coisa da validar float Agora apenas verifica se a palavra esta contida no set {"Alface", "Tomate", "Cenoura"}

registrar()

Coleta dados validados (tipo, quantidade, preço). Cria um dicionário com os dados formatados. Atualiza o arquivo JSON com o novo registro. Salva no Oracle (se conectado). Verifica alertas de estoque após o registro.

saldo_atual()

retorna um dicionário com os saldos calculados de cada tipo

listar_historico()

Lista o histórico de operações (entradas/saídas) de forma organizada. Usa alinhamento e casas decimais fixas para melhor legibilidade. Verifica se há dados antes de tentar exibi-los.

mostrar_saldo()

recebe o dicionário saldo atual vindo da função saldo atual verifica se existe conteúdo, caso não exibe um print caso exista faz um for no dicionário recebido usando .items() neste for temos t, q que recebem respectivamente chave e valor depois são printados e tabulados

verificar alerta()

Recebe o dicionário atual verifica o mínimo aceitável por produto verifica o saldo atual com o mínimo estando abaixo exibe o print


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- "Sem pastas separadas"

*Baixe os arquivos "ControleEstoque.py" e "SUBALGORITMOS.py" na mesma pasta, em seguida dentro do arquivo "SUBALGORITMOS.py", altere minhas informações de login do oracle em: 
ORACLE_USER = ""          
ORACLE_PASS = "" 
ORACLE_DSN  = "oracle.fiap.com.br:1521/ORCL" 
Insira seus dados e em seguida crie uma tabela chamada COLHEITAS no seu banco de dados oracle, agora é só rodar "ControleEstoque.py" e esta pronto :)


## 🗃 Histórico de lançamentos

* 0.1.0 - 20/04/2024
    

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


