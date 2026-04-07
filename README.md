# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioIA - Fase 2: Diagnóstico Automatizado

## 👨‍🎓 Integrantes: 
- <a href="#">Kleber Foks (RM: 562225 / Turma: 2TIAOA)</a>

## 📜 Descrição
Este projeto soluciona o desafio integrador da **Fase 2 do CardioIA** atuando no Diagnóstico Automatizado de pacientes triados em Pronto Atendimento. 

A arquitetura foi rigorosamente separada em duas abordagens de Inteligência Artificial:
1. **Modelagem de Regras (Parte 1):** Extração estruturada de sintomas relatados na linguagem natural usando correspondências baseadas em Ontologia (Sistemas Especialistas).
2. **Machine Learning e Viés Algorítmico (Parte 2):** Implementação e treinamento de um classificador de risco (Regressão Logística). Aplicou-se também técnicas avançadas de processamento (`TfidfVectorizer` do *Scikit-learn*), refletindo com total transparência sobre *Underfitting* e viés de Falsos Positivos causados por bases de dados estreitas.

> **Vídeo de Demonstração (YouTube):** [https://youtu.be/UuTJxS9J9BU]

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Arquivos de configuração específicos do GitHub (A auto-gerar).
- <b>assets</b>: Arquivos relacionados a elementos não-estruturados, como a logo acima.
- <b>config</b>: Arquivos de configuração paramétricos do ambiente.
- <b>document</b>: **DATA GOVERNANCE (Base do Projeto):**
  Apoiando-se no feedback avaliativo, dividimos em absoluto escopo a taxonomia e as fontes de todos os nossos 3 Dados Injetados em `.csv` e `.txt`:
  - *Dado 1 (Mapeamento Tabelar):* `src/parte1/mapa_conhecimento.csv`. É nossa tabela estruturada relacionando Doenças.
  - *Dado 2 (Brutos/Textuais):* `src/parte1/sintomas.txt`. Variáveis qualitativas sintéticas simulando fala humana.
  - *Dado 3 (Relacional de ML):* `src/parte2/dataset_risco.csv`. Features de strings curtas supervisionadas em alvo categórico.
- <b>src</b>: **Diretório do Código Fonte**. Os módulos exigidos:
  - `src/parte1/analisador_sintomas`: Scrip Python contendo o raciocínio matemático de intersecções/parsing lógico.
  - `src/parte2/triagem_modelo` e `comparativo_vies`: Cérebros analíticos de modelagem estatística testando o peso do TF-IDF.
  - `src/CardioIA_Desafio_Completo.ipynb`: Arquivo supremo no formato Jupyter Notebook.
- <b>README.md</b>: Este guia central da entrega.

## 🔧 Como executar o código

**Pré-requisitos:** Python 3.x puro instalado no ambiente Windows/Linux, além dos escopos das bibliotecas `pandas` e `scikit-learn` baixados ativamente. 

1. Baixe o código fonte e abra a raiz no terminal / VS Code.
2. Certifique-se de realizar o download das libs de processamento numérico digitando: `pip install pandas scikit-learn`
3. Execute o extrator textual da rotina Parte 1: `python src/parte1/analisador_sintomas.py`
4. Execute o validador estatístico da Parte 2: `python src/parte2/triagem_modelo.py`
5. Acione o script Bônus do laboratório mitigador de Viés/Falsos Positivos da Parte 2 ativando em tempo real: `python src/parte2/comparativo_vies.py`
6. **Deploy Prático para Notebook (.ipynb):** Realize upload solitário do arquivo gigante unificado `src/CardioIA_Desafio_Completo.ipynb` no painel aberto do **Google Colab**. Mova o `.csv` e o `.txt` para perto dele em nuvem e aperte "Play".

## 🗃 Histórico de lançamentos

* 0.1.0 - 06/04/2026
    * Desafio Entregue; Modelos de NLP, Parsing Rule-Based e Classificadores ML com base expansiva aplicados sobre o CardioIA Fase 2.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
