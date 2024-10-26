import pandas as pd
import os

# Verifica se os arquivos df_despesas.csv e df_receitas.csv existem
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    # Lê os arquivos CSV especificando a coluna de data
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=["Data"])
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=["Data"])
    
    # Se você quiser garantir que a coluna "Data" esteja no formato de data
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"], errors="coerce").dt.date
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"], errors="coerce").dt.date

else:
    # Estrutura de dados inicial caso os arquivos não existam
    data_structure = {
        'Valor': [],
        'Efetuado': [],
        'Fixo': [],
        'Data': [],
        'Categoria': [],
        'Descrição': [],
    }

    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv", index=False)  # Adiciona index=False
    df_receitas.to_csv("df_receitas.csv", index=False)  # Adiciona index=False


# Verifica se os arquivos de categorias de receita e despesa existem
if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()

else:    
    # Define categorias iniciais caso os arquivos não existam
    cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]}
    
    df_cat_receita = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_receita.to_csv("df_cat_receita.csv", index=False)  # Adiciona index=False
    df_cat_despesa.to_csv("df_cat_despesa.csv", index=False)  # Adiciona index=False
