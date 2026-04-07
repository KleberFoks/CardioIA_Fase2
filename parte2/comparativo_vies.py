import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def treinar_modelo(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv, encoding='utf-8')
    except Exception as e:
        print(f"Erro ao ler {caminho_csv}: {e}")
        return None, None
        
    X = df['frase']
    y = df['situacao'].str.strip()
    
    vetorizador = TfidfVectorizer()
    # Adquirindo vocabulário
    X_vet = vetorizador.fit_transform(X)
    
    modelo = LogisticRegression(random_state=42)
    modelo.fit(X_vet, y)
    
    # Acurácia no próprio dataset apenas para validar se aprendeu e os pesos não estão zerados
    acc = accuracy_score(y, modelo.predict(X_vet))
    
    return vetorizador, modelo, acc, len(df)

def main():
    print("-------------------------------------------------------------------------")
    print("      LABORATÓRIO: O IMPACTO DO VIÉS DE DADOS (DATA GOVERNANCE)          ")
    print("-------------------------------------------------------------------------\n")
    
    print("[1] Treinando Inteligência A: Base de Dados Pobre (Problema Antigo)")
    vet_ruim, mod_ruim, acc_ruim, len_ruim = treinar_modelo("dataset_risco.csv")
    print(f" -> Modelo treinado com apenas {len_ruim} linhas.")
    
    print("\n[2] Treinando Inteligência B: Base de Dados Expandida (Governança Aplicada)")
    vet_bom, mod_bom, acc_bom, len_bom = treinar_modelo("dataset_risco_expandido.csv")
    print(f" -> Modelo treinado com {len_bom} linhas mais detalhadas.")
    
    print("\n=========================================================================")
    print("   DESAFIO PRÁTICO: O PACIENTE FOI PRA TRIAGEM DO HOSPITAL               ")
    print("=========================================================================\n")
    
    frases_teste = [
        "Sinto muito peso no meu peito, a dor está esmagando meu braço.",
        "Meu joelho está ralado depois de um tombo de bicicleta que levei ontem.",
        "To com uma falta de ar subita na sala.",
        "dor passageira no punho de tanto digitar no pc velho."
    ]
    
    for frase in frases_teste:
        print(f"Paciente chega e diz: \"{frase}\"")
        
        # Testando no modelo pobre
        vet1 = vet_ruim.transform([frase])
        pred1 = mod_ruim.predict(vet1)[0]
        
        # Testando no modelo enriquecido
        vet2 = vet_bom.transform([frase])
        pred2 = mod_bom.predict(vet2)[0]
        
        # Conferindo se eles discordam
        if pred1 == pred2:
            print(f"   [Ambos os Modelos Concordaram] -> {pred2.upper()}\n")
        else:
            print(f"   -> DIVERGÊNCIA IDENTIFICADA!")
            print(f"      - A Inteligência Pobre (Viés) apontou: {pred1.upper()}")
            print(f"      - A Inteligência Maior corrigiu para : {pred2.upper()}\n")

if __name__ == "__main__":
    main()
