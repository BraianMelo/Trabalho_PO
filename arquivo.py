import re

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]
    return processar_linhas(linhas)

def processar_linhas(linhas):
    problema = {
        "tipo": extrair_tipo_objetivo(linhas[0]),
        "objetivo": extrair_funcao_objetivo(linhas[0]),
        "restricoes": extrair_restricoes(linhas[1:-1]),
        "limites": extrair_limites(linhas[-1])
    }

    print(problema)
    return problema

def extrair_tipo_objetivo(linha):
    linha = linha.lower()
    if linha.startswith("max"):
        return "Maximização"
    elif linha.startswith("min"):
        return "Minimização"
    else:
        raise ValueError("A primeira linha deve começar com 'max' ou 'min'.")

def extrair_funcao_objetivo(linha):
    expressao = linha.split('=')[1]
    termos = re.findall(r'([+-]?\s*\d*\.?\d*\s*x\d+)', expressao)
    objetivo = {}
    for termo in termos:
        termo = termo.replace(' ', '')
        coef_str, var = re.split(r'x', termo)
        coef = float(coef_str) if coef_str not in ('', '+', '-') else float(coef_str + '1')
        objetivo['x' + var] = coef
    return objetivo

def extrair_restricoes(linhas_restricoes):
    restricoes = []
    for linha in linhas_restricoes:
        linha_sem_espacos = linha.replace(' ', '')
        match = re.match(r'(.*)(<=|>=|=)(.*)', linha_sem_espacos)
        if not match:
            raise ValueError(f"Restrição mal formatada: {linha}")
        lhs, operador, rhs = match.groups()
        termos = re.findall(r'([+-]?\d*\.?\d*x\d+)', lhs)
        restricao = {"coef": {}, "op": operador, "b": float(rhs)}
        for termo in termos:
            coef_str, var = re.split(r'x', termo)
            coef = float(coef_str) if coef_str not in ('', '+', '-') else float(coef_str + '1')
            restricao["coef"]['x' + var] = coef
        restricoes.append(restricao)
    return restricoes

def extrair_limites(linha):
    return set(re.findall(r'(x\d+)\s*>=\s*0', linha))

ler_arquivo("entrada.txt")