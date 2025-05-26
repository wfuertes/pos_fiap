# Tech Challenge - Modelo Preditivo de Custos Médicos

Este repositório contém a solução para o Tech Challenge, que consiste no desenvolvimento de um modelo preditivo de regressão para prever o valor dos custos médicos individuais cobrados pelo seguro de saúde.

## Estrutura do Projeto

```
tech_challenge_01/
│
├── data/                      # Diretório com os dados utilizados
│   └── dataset-tech-challenge.csv  # Dataset com informações dos segurados
│
├── notebooks/                 # Diretório com os notebooks Jupyter
│   └── tech_challenge_notebook.ipynb  # Notebook principal com explicações
│
└── README.md                  # Este arquivo
```

## Requisitos

Para executar o notebook, você precisará das seguintes bibliotecas Python:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels
- scipy

Você pode instalar todas as dependências necessárias usando o comando:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels scipy
```

## Como Usar o Notebook

1. Clone este repositório para sua máquina local:
   ```bash
   git clone <url-do-repositorio>
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd tech_challenge
   ```

3. Inicie o Jupyter Notebook ou JupyterLab:
   ```bash
   jupyter notebook
   # ou
   jupyter lab
   ```

4. Abra o notebook `notebooks/tech_challenge_notebook_com_explicacoes.ipynb`

5. Execute as células sequencialmente para:
   - Explorar os dados
   - Realizar o pré-processamento
   - Criar e treinar os modelos de regressão
   - Validar estatisticamente os resultados
   - Visualizar e analisar os resultados

## Descrição do Notebook

O notebook está estruturado nas seguintes seções:

### 1. Exploração de dados
- **1.1 Base de dados e suas características**: Análise inicial do dataset, incluindo tipos de dados, valores ausentes e distribuição das variáveis categóricas.
- **1.2 Análise estatísticas descritivas e visualizações**: Estatísticas descritivas e visualizações para entender a distribuição das variáveis e suas relações.

### 2. Pré-processamento de dados
- **2.1 Limpeza dos dados e tratamento de valores ausentes**: Verificação e tratamento de valores ausentes e inconsistentes.
- **2.2 Conversão de variáveis categóricas**: Transformação de variáveis categóricas em formatos adequados para modelagem.

### 3. Modelagem
- **3.1 Criação do modelo preditivo de regressão**: Definição das variáveis preditoras e da variável alvo.
- **3.2 Divisão do conjunto de dados**: Separação em conjuntos de treinamento e teste.
- **3.3 Treinamento do modelo**: Treinamento e avaliação de modelos de Regressão Linear e Random Forest.
- **3.4 Validação estatística**: Análise detalhada dos coeficientes, significância estatística e pressupostos do modelo.

### 4. Resultados
- **4.1 Apresentação de resultados visuais**: Visualizações comparando valores reais e previstos.
- **4.2 Relatório com análise dos resultados**: Relatório detalhado com insights, conclusões e recomendações.

## Sobre os Dados

O dataset contém informações sobre segurados de saúde, incluindo:
- Idade
- Gênero
- IMC (Índice de Massa Corporal)
- Número de filhos
- Status de fumante
- Região de residência
- Encargos médicos (variável alvo)

## Resultados e Insights

Os principais insights obtidos da análise incluem:

1. O status de fumante é o fator mais impactante nos custos médicos
2. A idade tem uma correlação positiva significativa com os encargos
3. O IMC também influencia positivamente os custos médicos
4. Existem variações regionais nos custos médicos

O modelo desenvolvido pode auxiliar seguradoras de saúde na estimativa mais precisa dos custos médicos individuais, permitindo uma precificação mais justa e personalizada dos planos de saúde.

## Autor

Este projeto foi desenvolvido como parte do Tech Challenge.
