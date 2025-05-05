# 🌍 Geolocalizador

O **Geolocalizador** é um projeto que une tecnologia e geografia para mostrar, de forma prática, como a localização geográfica pode ser usada em sistemas modernos. Seja para encontrar um local, rastrear um objeto ou simplesmente entender o espaço à nossa volta.

## 🧭 Sobre o Projeto

Este sistema utiliza Python e a biblioteca "geopy" para converter endereços em **coordenadas geográficas** (latitude e longitude), com base em um arquivo CSV de endereços. É uma forma prática de aplicar conceitos geográficos usando dados reais.

---

## ⚙️ Tecnologias Utilizadas

- Python
- [pandas](https://pandas.pydata.org/)
- [geopy](https://geopy.readthedocs.io/)
- API Nominatim (OpenStreetMap)

---

## 🚀 Como Usar
Antes de tudo, prepare o arquivo de entrada:

- O arquivo deve ser um CSV com separador ;
- Nomeie as colunas como: rua, bairro, municipio, estado
- Evite acentos e caracteres especiais (ex: "São José" ➜ "Sao Jose", "Trav. João N." ➜ "Trav Joao N")
- Salve como enderecos.csv no mesmo diretório do script
- **Importante:** Se a sua tabela contém mais informações além dos campos necessários, é conselhavel extrair apenas as colunas com as informações que serão trabalhadas no código, para evitar erros. Após conseguir geocodificar, você pode fazer um join entre as tabelas. Daí, então, gerar os pontos a partir da geocodificação.

## 2. Instale as bibliotecas necessárias
Você pode usar o terminal ou o Jupyter Notebook:

Utilize este comando no terminal -->> **pip install pandas geopy**

## 3. Execute o script Python

## 4. Leia, é importante!

- Use dados limpos: sem acentos, símbolos ou abreviações confusas
- A API Nominatim tem limites de requisições por segundo. O RateLimiter foi configurado para evitar bloqueios. Normalmente ele realiza uma geocodificação por seg. Portanto, se tiver uma base de dados grande, será necessário esperar um tempo maior de execução.
- Para grandes volumes de endereços, considere usar serviços pagos com maior desempenho (como Google Maps API)
