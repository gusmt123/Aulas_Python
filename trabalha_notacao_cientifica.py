import pandas as pd

# Carrega o arquivo Excel
df = pd.read_excel('notacao_cientifica.xlsx', sheet_name=None)

# Itera sobre cada aba da planilha
for sheet_name, sheet_df in df.items():
    # Verifica se há colunas com valores em notação científica
    scientific_columns = sheet_df.select_dtypes(include=['float']).columns
    for col in scientific_columns:
        sheet_df[col] = sheet_df[col].apply(lambda x: float(x))

# Salva as alterações no arquivo Excel
with pd.ExcelWriter('notacao_cientifica_sem_notacao.xlsx') as writer:
    for sheet_name, sheet_df in df.items():
        sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Notações científicas transformadas em números sem notação científica para todas as abas.")
