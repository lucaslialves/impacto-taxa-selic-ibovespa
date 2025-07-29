<<<<<<< HEAD
# 📊 Impacto da Taxa Selic e das Reuniões do COPOM sobre o Desempenho do Ibovespa

## 📌 Contexto Profissional Simulado

Este projeto simula uma situação real da Tesouraria do Bradesco, onde atuo como Analista de Mercado.

O gestor da mesa de Renda Fixa solicitou um estudo quantitativo para compreender **como as decisões do COPOM**, por meio da **variação da Taxa Selic**, influenciam o comportamento do **Ibovespa** nos períodos subsequentes.

---

## 🎯 Objetivo de Negócio

Gerar **insights práticos e baseados em dados** que apoiem decisões estratégicas da Tesouraria, com foco em:

- Alocação tática de recursos
- Estratégias de proteção (hedge)
- Recomendação de produtos financeiros baseados em cenários de política monetária

---

## 👥 Stakeholders Envolvidos

- Mesa de Renda Fixa  
- Área de Produtos de Investimentos  
- Equipe de Riscos de Mercado  

---

## ❓ Pergunta SMART Principal

| Critério | Definição |
|---------|-----------|
| **Specific (Específica)** | Como a **variação da Taxa Selic definida nas reuniões do COPOM** impacta o **retorno acumulado do índice Ibovespa nos 45 dias úteis seguintes**? |
| **Measurable (Mensurável)** | A relação será medida por meio do **coeficiente de correlação de Pearson** e visualizações de dispersão. |
| **Achievable (Atingível)** | Utiliza dados históricos acessíveis entre **2013 e 2022**. |
| **Relevant (Relevante)** | A compreensão dessa relação é essencial para decisões da Tesouraria em cenários de aperto ou afrouxamento monetário. |
| **Time-bound (Temporal)** | Período de análise: **Janeiro/2013 a Dezembro/2022** |

---

## 🗂️ Dados Utilizados

- **Fonte:** Dataset [brazilian-stock-market](https://www.kaggle.com/datasets) (Kaggle)
- **Variáveis utilizadas:**
  - Datas e decisões das reuniões do **COPOM (Taxa Selic meta)**
  - Fechamento diário do **Ibovespa**
- *Observação:* Outros indicadores macroeconômicos (ex: IPCA, PIB) foram intencionalmente excluídos para manter o foco exclusivo na política monetária.

---

## 🛠️ Metodologia

1. **Compreensão do problema e requisitos do negócio**
2. **Formulação de hipóteses e perguntas SMART**
3. **Importação e limpeza dos dados** (`pandas`, `numpy`)
4. **Alinhamento entre datas de reuniões do COPOM e a série histórica do Ibovespa**
5. **Cálculo do retorno acumulado do Ibovespa nos 45 dias úteis após cada reunião**
6. **Análise estatística (correlação, média, dispersão)**
7. **Visualizações com `matplotlib` e `seaborn`**
8. **Desenvolvimento de dashboard no Power BI**
9. **Conclusões e recomendações para os stakeholders**

---

## ✅ Status Atual do Projeto

- ✅ Definição do escopo e objetivos
- ✅ Coleta e organização dos dados
- ✅ Análise Exploratória em andamento
- ✅ Cálculo e interpretação estatística
- ✅ Criação de visualizações
- ✅ conclusões e recomendações

---

## Conclusão da Análise Exploratória (EDA)

Após analisar a relação entre as variações da Taxa Selic nas reuniões do COPOM e o retorno acumulado do Ibovespa nos 45 dias úteis seguintes, chegamos às seguintes conclusões:

- Não há evidências estatísticas suficientes para afirmar que existe uma correlação significativa entre as variações da Selic e o desempenho do Ibovespa nesse período.
- A correlação observada foi baixa e negativa (-0,19) e pode ter ocorrido por acaso, considerando um nível de confiança de 95%.
- Esse resultado sugere que, no curto prazo após as decisões de política monetária, o impacto direto da Selic sobre o mercado acionário brasileiro não é claro.

Deixo claro que este estudo foi uma simulação simples, realizada com fins de aprendizado em Python. Reconheço que o estudo teve limitações, incluindo um viés amostral significativo, pois, ao analisar o índice Ibovespa, diversas outras variáveis influenciam diretamente seu comportamento, como taxa de câmbio, inflação, cenários externos, entre outros.


## ▶️ Como Executar o Projeto

1. Clone este repositório ou baixe os notebooks localmente.
2. Instale as bibliotecas necessárias com o seguinte comando:

```bash
pip install pandas numpy matplotlib seaborn statsmodels yfinance scikit-learn fsspec



=======
# impacto-taxa-selic-ibovespa
Impacto da politica monetaria no Desempenho do Mercado de Ações Brasileiro (B3)
>>>>>>> 3c6dab410194030e2398fc4a2c751db66417413b
