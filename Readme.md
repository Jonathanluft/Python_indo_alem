A solução busca controlar o estoque de 3 culturas produzidas,
quando abaixo do nível mínimo aceitável exibe um alerta.

além disso salva todos os registros em um arquivo json e adiciona as informações em uma banco de dados usando SQL.

SUBALGORITMOS:

ler_json()

Verifica existência do arquivo:
Se não existe → Retorna [].
Se existe → Abre o arquivo e lê seu conteúdo.
Converte o JSON para uma estrutura Python (lista de dicionários).
Retorna a estrutura (lista de dicionários).

salvar_json()

Abre o arquivo em modo de escrita (cria se não existir).
Converte a lista de dicionários para JSON com formatação amigável.
Salva os dados no arquivo e fecha automaticamente

inserir Oracle()

Tenta conectar ao Oracle e inserir o registro.
Se ocorrer erro Exibe detalhes do erro.
Se tudo der certo Os dados são salvos na tabela COLHEITAS.

validar_float()

Recebe uma string
Faz um loop infinito e entra em um try
Recebe o valor do user e tenta converter pra float
Caso não consiga exibe "Digite número válido!"

validar tipo()

Basicamente a mesma coisa da validar float
Agora apenas verifica se a palavra esta contida no set
{"Alface", "Tomate", "Cenoura"}

registrar()

Coleta dados validados (tipo, quantidade, preço).
Cria um dicionário com os dados formatados.
Atualiza o arquivo JSON com o novo registro.
Salva no Oracle (se conectado).
Verifica alertas de estoque após o registro.


saldo_atual()

retorna um dicionário com os saldos calculados de cada tipo


listar_historico()

Lista o histórico de operações (entradas/saídas) de forma organizada.
Usa alinhamento e casas decimais fixas para melhor legibilidade.
Verifica se há dados antes de tentar exibi-los.

mostrar_saldo()

recebe o dicionário saldo atual vindo da função saldo atual
verifica se existe conteúdo, caso não exibe um print
caso exista faz um for no dicionário recebido usando .items()
neste for temos t, q que recebem respectivamente chave e valor
depois são printados e tabulados

verificar alerta()

recebe o dicionário atual 
verifica o mínimo aceitável por produto
verifica o saldo atual com o mínimo
estando abaixo exibe o print
