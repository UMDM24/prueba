
---

# 🍽️ Meal API Wrapper

Este proyecto es una aplicación **Full Stack** que actúa como un puente (wrapper) para consumir datos de [TheMealDB](https://www.themealdb.com/api.php). Proporciona una interfaz simplificada y estandarizada a través de un backend en **FastAPI** y un frontend interactivo con **Vanilla JS**.

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una estructura modular para facilitar el mantenimiento:

* **Backend (`app/`)**: Construido con FastAPI, utiliza routers independientes para organizar los endpoints.
* **Servicios**: Lógica centralizada para peticiones externas usando `httpx`.
* **Transformers**: Limpieza y normalización de la respuesta cruda de la API externa para entregar un JSON más amigable al frontend.
* **Frontend**: Interfaz sencilla en HTML5, CSS3 y JavaScript.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x, FastAPI, Uvicorn, HTTPX (Peticiones asíncronas).
* **Seguridad/Configuración:** `python-dotenv` para variables de entorno y Middleware CORS.
* **Frontend:** HTML, CSS, JavaScript (Fetch API).

---

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <tu-url-del-repositorio>
cd DIPLOMADO_1RA

```

### 2. Configurar el Entorno Virtual

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt

```

### 4. Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto basándote en la lógica de `config.py`:

```env
THEMEALDB_BASE_URL=https://www.themealdb.com/api/json/v1/1
TIMEOUT=10

```

---

## 🖥️ Ejecución

### Iniciar el Backend

Desde la raíz del proyecto, ejecuta:

```bash
uvicorn main:app --reload

```

La API estará disponible en: `http://127.0.0.1:8000`. Puedes revisar la documentación interactiva en `http://127.0.0.1:8000/docs`.

### Iniciar el Frontend

Simplemente abre el archivo `Frontend/index.html` en tu navegador favorito.

---

## 🛣️ Endpoints Principales (API)

| Método | Endpoint | Descripción |
| --- | --- | --- |
| `GET` | `/meals/search?name={valor}` | Busca recetas por nombre. |
| `GET` | `/meals/letter/{letra}` | Busca recetas que inicien con una letra. |
| `GET` | `/filters/category/{cat}` | Filtra recetas por categoría. |
| `GET` | `/lists/categories/all` | Obtiene el listado completo de categorías. |
| `GET` | `/lists/areas` | Obtiene el listado de países/áreas. |

---

## 📁 Estructura de Carpetas

```text
.
├── app/
│   ├── core/           # Configuración y variables de entorno.
│   ├── routers/        # Definición de rutas (meals, filters, lists).
│   ├── services/       # Cliente HTTP para TheMealDB.
│   └── utils/          # Transformadores de datos.
├── Frontend/           # Interfaz de usuario (HTML, CSS, JS).
├── .env                # Variables sensibles.
├── main.py             # Punto de entrada de FastAPI.
└── requirements.txt    # Dependencias del proyecto.

```

---
