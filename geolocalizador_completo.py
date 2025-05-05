import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Lê o CSV com separador ";"
df = pd.read_csv('enderecos.csv', sep=';')
df.columns = df.columns.str.strip().str.lower()  # Normaliza os nomes das colunas

# Configura o geolocalizador
geolocator = Nominatim(user_agent="geoapi")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Função para obter coordenadas a partir do endereço completo
def get_coordinates(row):
    endereco = f"{row['rua']}, {row['bairro']}, {row['municipio']}, {row['estado']}, Brasil"
    location = geocode(endereco)
    if location:
        return pd.Series([location.latitude, location.longitude])
    else:
        return pd.Series([None, None])

# Aplica a função ao DataFrame
df[['latitude', 'longitude']] = df.apply(get_coordinates, axis=1)

# Salva o resultado
df.to_csv('enderecos_com_coordenadas.csv', index=False)

print("Arquivo 'enderecos_com_coordenadas.csv' criado com sucesso!")
