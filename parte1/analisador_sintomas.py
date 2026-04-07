import csv

def carregar_mapa(caminho_csv):
    """
    Lê o arquivo CSV e retorna uma lista de dicionários com as regras (Sintoma 1, Sintoma 2 -> Doença).
    """
    mapa = []
    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linha in reader:
                mapa.append({
                    'sintoma1': linha['Sintoma 1'].strip().lower(),
                    'sintoma2': linha['Sintoma 2'].strip().lower(),
                    'doenca': linha['Doença Associada'].strip()
                })
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")
    return mapa

def carregar_frases(caminho_txt):
    """
    Lê o arquivo TXT com os relatos dos pacientes ignorando linhas em branco.
    """
    try:
        with open(caminho_txt, mode='r', encoding='utf-8') as f:
            # Retorna uma lista limpando espaços vazios
            return [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_txt} não foi encontrado.")
        return []

def analisar(frases, mapa):
    """
    Analisa os sintomas de cada frase em base comparativa com o mapa (Rule-based NLP).
    """
    print("-------------------------------------------------------------------------")
    print("       DIAGNÓSTICO AUTOMATIZADO - MÓDULO INTELIGENTE (FASE 2)          ")
    print("-------------------------------------------------------------------------\n")

    for i, frase in enumerate(frases, 1):
        print(f"[Paciente {i} Relato] -> \"{frase}\"")
        frase_lower = frase.lower()
        
        diagnosticos_encontrados = set()
        sintomas_detectados = set()

        for regra in mapa:
            # Procuramos se a string da frase possui os sintomas-chave mapeados
            s1_presente = regra['sintoma1'] in frase_lower
            s2_presente = regra['sintoma2'] in frase_lower
            
            if s1_presente: 
                sintomas_detectados.add(regra['sintoma1'])
            if s2_presente: 
                sintomas_detectados.add(regra['sintoma2'])
            
            # Condição Básica para a Onotologia Médica do Exercício:
            # Se o sintoma 1 OU o sintoma 2 estiverem na frase, levanta o alerta da respectiva doença.
            if s1_presente or s2_presente:
                diagnosticos_encontrados.add(regra['doenca'])

        # Se a IA por regras mapeou alguma coisa...
        if diagnosticos_encontrados:
            print(f" -> Sintomas identificados: {', '.join(sintomas_detectados)}")
            print(f" -> Possível Diagnóstico Assistido: {', '.join(diagnosticos_encontrados)}\n")
        else:
            print(" -> Sintomas identificados: Nenhum mapeado na ontologia.")
            print(" -> Possível Diagnóstico Assistido: Encaminhar para triagem manual médica (Fora do Mapa).\n")


if __name__ == "__main__":
    # Carregando conhecimento
    mapa_db = carregar_mapa("mapa_conhecimento.csv")
    frases_relatadas = carregar_frases("sintomas.txt")
    
    # Processando
    if mapa_db and frases_relatadas:
        analisar(frases_relatadas, mapa_db)
