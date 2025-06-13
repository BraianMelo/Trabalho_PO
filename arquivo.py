import json;

def ler_arquivo(caminho):
    with open(caminho, 'r') as arquivo:
        dicionario = json.load(arquivo);
    return dicionario;

def extrair_dados(dicionario):
    tipo = dicionario.get("problema");
    qtd_variaveis = len(dicionario["variaveis"]);
    expressao = dicionario.get("funcao_objetivo").get("expressao");
    restricoes_dict = dicionario.get("restricoes");
    restricoes = [];

    for i in restricoes_dict:
        restricoes.append(i.get("expressao"));
    
    print(f"{tipo}: {expressao} ({qtd_variaveis} variáveis)");
    print("restrições:")
    for i in restricoes:
        print(i);


dicionario = ler_arquivo("entrada.json");
extrair_dados(dicionario);