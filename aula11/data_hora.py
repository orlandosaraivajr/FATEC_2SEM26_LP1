from datetime import datetime

agora = datetime.now()
print("Data e hora atuais:", agora)

# Exibindo apenas a data em formato brasileiro
data_formatada = agora.strftime("%d/%m/%Y")
print("Data formatada:", data_formatada)

# Exibindo data e hora com formato personalizado
completo = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data e hora formatadas:", completo)

data_str = "28/05/2025 14:30:00"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print("String convertida para datetime:", data_convertida)

inicio = datetime.strptime("01/01/2025", "%d/%m/%Y")
fim = datetime.strptime("28/05/2025", "%d/%m/%Y")
diferenca = fim - inicio
print("Diferença de dias:", diferenca.days)

