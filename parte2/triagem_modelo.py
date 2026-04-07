import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    print("-------------------------------------------------------------------------")
    print("     TREINAMENTO IA: CLASSIFICADOR DE RISCO (NLP + TF-IDF) - FASE 2      ")
    print("-------------------------------------------------------------------------\n")

    # 1. Carregar base de dados
    try:
        df = pd.read_csv("dataset_risco.csv", encoding="utf-8")
        print(f"[OK] Base de Dados Carregada: {len(df)} registros encontrados.")
    except Exception as e:
        print(f"[ERRO] Falha ao carregar CSV: {e}")
        return
        
    print("\n[Amostra dos Dados de Triagem Inicial]")
    print(df.head(3))
    
    # 2. Separar as features (x = frases) e os alvos (y = situação)
    X = df['frase']
    y = df['situacao'].str.strip() # Limpa os possiveis espacos
    
    # 3. Processamento de Linguagem Natural (TF-IDF Vectorizer)
    # Transforma texto em vetores de importância matemática com base na frequência das palavras
    vetorizador = TfidfVectorizer()
    X_vetorizado = vetorizador.fit_transform(X)
    
    # Exibir quantas colunas (palavras exclusivas) nosso vocabulário tem
    print(f"\n[TF-IDF] Vocabulário montado com {X_vetorizado.shape[1]} palavras únicas.")
    
    # 4. Dividir Base em Treino e Teste
    # Pegamos 30% pro teste como validação e 70% pro computador aprender
    X_treino, X_teste, y_treino, y_teste = train_test_split(X_vetorizado, y, test_size=0.3, random_state=42)
    
    # 5. Treinando o Classificador de Machine Learning
    print("\n[Treinamento] Construindo o modelo Logistic Regression (Scikit-Learn)...")
    
    # Usando Logist Regression devido ao dataset ser bem pequeno e puramente textual (Binario).
    # Caso prefira arvore de decisao, descomente a linha abaixo e comente a de cima!
    modelo = LogisticRegression(random_state=42)
    # modelo = DecisionTreeClassifier(random_state=42) 
    
    modelo.fit(X_treino, y_treino)
    
    # 6. Previsões e Métricas
    previsoes = modelo.predict(X_teste)
    acuracia = accuracy_score(y_teste, previsoes)
    
    print(f"\n[RESULTADOS DO MODELO DE TRIAGEM]")
    print(f" -> Acurácia Geral do Sistema: {acuracia * 100:.2f}%")
    
    print("\n[Relatório de Classificação Detalhado]")
    print(classification_report(y_teste, previsoes, zero_division=0))
    
    # 7. Simulador Interativo: Testando com frases nunca antes vistas pela IA
    frases_invisiveis_ao_treino = [
        "Sinto muito peso no meu peito, dor forte que está esmagando meu braço.",
        "Meu joelho está raspado depois de um tombo de bicicleta que levei ontem.",
        "To com uma falta de ar subita na sala.",
        "dor passageira no punho digitando muito"
    ]
    
    print("\n------------------------------------------------------------------")
    print("[Inferência (Real-Time)] - Testando em Frases Ocultas Inéditas")
    print("------------------------------------------------------------------")
    
    # O pipeline obriga passarmos os dados novos pelo mesmo filtro TF-IDF
    vetores_novos = vetorizador.transform(frases_invisiveis_ao_treino)
    diagnosticos = modelo.predict(vetores_novos)
    
    for frase, classe in zip(frases_invisiveis_ao_treino, diagnosticos):
        print(f"Frase: '{frase}'\n   [SISTEMA APONTA: {classe.upper()}]\n")
        
if __name__ == "__main__":
    main()
