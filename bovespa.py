# https://gist.github.com/rodrigobercini/8bbee7fc735ad7d696f7a2ec31df9610
from yahooquery import Ticker

# Período máximo
petr = Ticker("PETR4.SA")
petr.history(period='max')

# Datas específicas
petr.history(start='2005-05-01', end='2013-12-31')

# Intraday - 30 minutos
abev = Ticker('ABEV3.SA')
abev.history(period='60d',  interval = "30m")

# Intraday - 1 minuto
abev = abev.history(period='7d',  interval = "1m")
print(abev)

# Informações financeiras
petr = Ticker("PETR4.SA")     # Coleta dados
petr = petr.income_statement()# Chama função de Demonstração de resultados
petr = petr.transpose()       # Transpõe a matriz
petr.columns = petr.iloc[0,:] # Renomeia colunas
petr = petr.iloc[2:,:-1]      # Seleciona dados
petr = petr.iloc[:, ::-1]     # Inverte colunas
print(petr)
