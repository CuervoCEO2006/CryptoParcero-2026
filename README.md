# CryptoCompadre-2026
**Estefany Arenas Carvajal**  
**Juan José Cuervo Osorio**  
**Juan José Camargo Chaverra**

---

## Caso de estudio: sistema de consulta financiera CryptoCompadre

Este ejercicio consiste en desarrollar un sistema de consulta financiera que opera a través de un bot de Telegram. El sistema permite a los usuarios obtener información básica sobre activos financieros como criptomonedas, acciones e índices bursátiles mediante comandos enviados en el chat.

Cuando el usuario inicia la interacción con el sistema utilizando el comando `/start` o `/inicio`, el bot responde con un mensaje de bienvenida. A partir de ese momento, el usuario puede interactuar con el sistema utilizando comandos específicos.

El sistema reconoce comandos como `/compadre`, que permite acceder a un menú de activos financieros disponibles, y `/syp500`, que permite consultar el valor actual del índice S&P 500. Si el usuario ingresa un comando no reconocido, el sistema informará que el comando es incorrecto. Si el usuario envía mensajes que no corresponden a comandos, el sistema indicará que solo acepta interacciones mediante comandos válidos.

Cuando el usuario utiliza el comando `/compadre`, el sistema presenta un conjunto de opciones que corresponden a diferentes activos financieros, tales como criptomonedas (por ejemplo, Bitcoin o Ethereum) y acciones (como Apple, Microsoft o Tesla). El usuario podrá seleccionar uno de estos activos para consultar su información.

Una vez seleccionado el activo, el sistema realiza una consulta a fuentes externas de datos financieros y obtiene la información correspondiente. El sistema mostrará al usuario el precio actual del activo, la moneda en la que se encuentra expresado y la variación porcentual reciente. Con base en esta variación, el sistema indicará si el comportamiento del activo es de subida, bajada o estabilidad.

Adicionalmente, el sistema consultará noticias relacionadas con el activo seleccionado o con el mercado financiero en general. Estas noticias serán presentadas al usuario en forma de título, fuente y enlace, permitiendo ampliar la información consultada.

El sistema también genera un gráfico histórico del comportamiento del activo en un intervalo de tiempo reciente. Este gráfico es enviado al usuario en formato de imagen dentro del chat, permitiendo visualizar la evolución del precio.

Si durante la ejecución de alguna de estas operaciones ocurre un error, como la inexistencia del activo consultado o la imposibilidad de obtener datos desde las APIs externas, el sistema informará al usuario y continuará disponible para nuevas consultas.

El sistema permanecerá en ejecución mientras el usuario continúe interactuando con el bot, permitiendo realizar múltiples consultas durante una misma sesión.

El diseño del sistema se basa en programación orientada a objetos, en donde se definen clases con responsabilidades específicas. La clase principal del bot se encarga de gestionar la interacción con Telegram, mientras que otras clases se encargan de obtener información financiera, consultar noticias y generar gráficos. Esta organización permite mantener el sistema modular y facilita su mantenimiento y extensión.

---

## Modelo del mundo

### 1. Identificación de entidades y características

**CryptoCompadre_Bot**
- token
- comandos disponibles

**Activo**
- symbol
- nombre
- tipo
- precio actual
- datos históricos

**Noticia**
- titulo
- enlace
- fuente

**Grafico**
- activo
- periodo
- imagen

---

## Requisitos funcionales

### 1. Identificación de requisitos

- Iniciar interacción
- Mostrar mensaje de bienvenida
- Mostrar menú principal
- Seleccionar activo financiero
- Consultar precio actual
- Mostrar variación porcentual
- Consultar noticias
- Generar gráfico histórico
- Consultar índice S&P 500
- Validar comandos incorrectos
- Manejar errores de consulta
- Permitir múltiples consultas

### 2. Especificación y descomposición de requisitos

#### 2.1 Requisito 1: Iniciar interacción

| | |
|---|---|
| **Nombre** | R1 – Iniciar interacción |
| **Resumen** | El sistema debe permitir al usuario iniciar la interacción con el bot mediante comandos de inicio. |
| **Entradas** | Comando `/start` o `/inicio` |
| **Resultado** | 1. El sistema muestra un mensaje de bienvenida al usuario <br> 2. El sistema presenta las opciones principales disponibles <br> 3. El sistema queda listo para recibir comandos |

**Descomposición:**

| Pasos | Métodos | Responsable |
|-------|---------|-------------|
| Iniciar interacción | `bienvenida_a_usuario(message)` | CryptoCompadre_Bot |
| Mostrar bienvenida | `send_message()` | CryptoCompadre_Bot |

#### 2.2 Requisito 2: Mostrar menú principal

| | |
|---|---|
| **Nombre** | R2 – Mostrar menú principal |
| **Resumen** | El sistema debe permitir mostrar al usuario un menú con las opciones disponibles para consultar información financiera. |
| **Entradas** | Comando `/compadre` |
| **Resultado** | 1. El sistema muestra un menú con activos financieros disponibles <br> 2. El sistema permite seleccionar un activo <br> 3. El sistema espera la selección del usuario |

**Descomposición:**

| Pasos | Métodos | Responsable |
|-------|---------|-------------|
| Mostrar menú | `compadre_menu()` | CryptoCompadre_Bot |
| Enviar menú | `send_message()` | CryptoCompadre_Bot |

#### 2.3 Requisito 3: Consultar precio actual

| | |
|---|---|
| **Nombre** | R3 – Consultar precio actual |
| **Resumen** | El sistema debe permitir consultar el precio actual de un activo financiero seleccionado. |
| **Entradas** | Selección de un activo (ej: BTC-USD, AAPL) |
| **Resultado** | 1. El sistema consulta la información del activo <br> 2. El sistema obtiene el precio actual <br> 3. El sistema muestra el precio al usuario |

**Descomposición:**

| Pasos | Métodos | Responsable |
|-------|---------|-------------|
| Consultar activo | `obtener_precio_actual()` | CryptoCompadre_Bot |
| Obtener datos | `yf.Ticker()` | Activo |
| Mostrar precio | `send_message()` | CryptoCompadre_Bot |

#### 2.4 Requisito 4: Consultar noticias

| | |
|---|---|
| **Nombre** | R4 – Consultar noticias |
| **Resumen** | El sistema debe permitir obtener noticias relacionadas con el activo seleccionado. |
| **Entradas** | Símbolo del activo |
| **Resultado** | 1. El sistema consulta noticias desde la API <br> 2. El sistema procesa la información obtenida <br> 3. El sistema muestra las noticias al usuario |

**Descomposición:**

| Pasos | Métodos | Responsable |
|-------|---------|-------------|
| Consultar activo | `obtener_precio_actual()` | CryptoCompadre_Bot |
| Obtener datos | `yf.Ticker()` | Activo |
| Mostrar precio | `send_message()` | CryptoCompadre_Bot |

#### 2.5 Requisito 5: Generar gráfico

| | |
|---|---|
| **Nombre** | R5 – Generar gráfico |
| **Resumen** | El sistema debe generar un gráfico histórico del comportamiento del activo seleccionado. |
| **Entradas** | Símbolo del activo |
| **Resultado** | 1. El sistema obtiene datos históricos del activo <br> 2. El sistema genera un gráfico <br> 3. El sistema envía el gráfico al usuario |

**Descomposición:**

| Pasos | Métodos | Responsable |
|-------|---------|-------------|
| Obtener datos históricos | `yf.download()` | GeneradorGrafico |
| Generar gráfico | `generar_grafico_precio()` | GeneradorGraficos |
| Enviar gráfico | `send_photo()` | CryptoCompadre_Bot |