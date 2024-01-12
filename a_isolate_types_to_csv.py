import pandas as pd 

# Salva em csv para análise
def operation_types_to_csv(operation_types):
    operation_types_series = pd.Series(operation_types)
    operation_types_series.rename('Operation Types', inplace=True)
    operation_types_series.to_csv('./Operation Types.csv', index=False, header=True)


years = (2021, 2022, 2023)
records_by_year = [pd.read_csv(f'./{year}/{year} - Binance Transaction Records.csv') for year in years] # Lista ded DataFrames
columns = records_by_year[0].columns # --> 'User_ID', 'UTC_Time', 'Account', 'Operation', 'Coin', 'Change', 'Remark'
operation_types_by_year = []

# Remove duplicação na coluna 'Operation' para cada ano, cria três numpy.ndarray e armazena eles em uma lista
# Transforma o numpy.ndarray em um Panda Series antes de inserir na lista
# Panda Series é um vetor unidimensional
for record in records_by_year:
    operation_types_by_year.append(pd.Series(record[columns[3]].unique()))

# Concatena os Panda Series em um único vetor unidimensional (axis = 0)
# Novamente remove duplicação dos tipos de operação
operation_types = pd.concat(operation_types_by_year, axis = 0)
operation_types = operation_types.unique()

operation_types_to_csv(operation_types)