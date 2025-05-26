import pandas as pd
import numpy as np

# --- Parâmetros ---
num_linhas = 5000

# Regiões e suas proporções (aproximadas conforme fornecido)
regioes = ['Sudeste', 'Nordeste', 'Sul', 'Norte', 'Centro-Oeste']
# Probabilidades: 42%, 27%, 14.74%, 8.54%, 8.02%
probabilidades_regioes = [0.42, 0.27, 0.1474, 0.0854, 0.0802]
# Ajustar probabilidades para somar exatamente 1 (opcional, numpy.random.choice lida com pequenas diferenças)
probabilidades_regioes = np.array(probabilidades_regioes) / np.sum(probabilidades_regioes)


# --- Geração de Dados ---

# Idade (ex: entre 18 e 80 anos)
idades = np.random.randint(18, 81, size=num_linhas)

# Gênero (aproximadamente 50/50)
generos = np.random.choice(['feminino', 'masculino'], size=num_linhas, p=[0.51, 0.49]) # Levemente mais feminino

# IMC (distribuição normal em torno de 28, com limites)
imcs = np.clip(np.random.normal(loc=28, scale=6, size=num_linhas), 15, 50)

# Filhos (mais provável ter 0, 1 ou 2)
num_filhos = np.random.choice([0, 1, 2, 3, 4, 5], size=num_linhas, p=[0.40, 0.25, 0.20, 0.10, 0.03, 0.02])

# Fumante (ex: 25% fumantes)
fumantes = np.random.choice(['não', 'sim'], size=num_linhas, p=[0.75, 0.25])

# Região (baseado nas probabilidades populacionais)
regioes_distribuidas = np.random.choice(regioes, size=num_linhas, p=probabilidades_regioes)

# Encargos (fórmula baseada nos outros fatores + aleatoriedade)
# Baseado em: idade, imc, filhos, fumante. Valores são exemplos.
encargos_base = 1000 # Custo mínimo base
encargos_idade = idades * 50
encargos_imc = np.maximum(0, (imcs - 25)) * 200 # Custo adicional para IMC > 25
encargos_filhos = num_filhos * 300
encargos_fumante = (fumantes == 'sim') * 15000 # Custo alto para fumantes
ruido_aleatorio = np.random.normal(0, 1500, num_linhas) # Variabilidade

encargos_totais = (encargos_base +
                   encargos_idade +
                   encargos_imc +
                   encargos_filhos +
                   encargos_fumante +
                   ruido_aleatorio)

# Garantir que encargos não sejam menores que um valor mínimo (ex: 500)
encargos_totais = np.maximum(500, encargos_totais)


# --- Criação do DataFrame ---
df = pd.DataFrame({
    'idade': idades,
    'gênero': generos,
    'imc': imcs.round(2), # Arredondar para 2 casas decimais
    'filhos': num_filhos,
    'fumante': fumantes,
    'região': regioes_distribuidas,
    'encargos': encargos_totais.round(2) # Arredondar para 2 casas decimais
})

# --- Exportar para CSV ---
nome_arquivo_csv = 'dataset_estudo_5000.csv'
df.to_csv(nome_arquivo_csv, index=False, encoding='utf-8')

print(f"Arquivo '{nome_arquivo_csv}' gerado com sucesso com {len(df)} linhas.")
print("\nPrimeiras 5 linhas do dataset gerado:")
print(df.head())