#  Motor de Búsqueda con TF-IDF

Este proyecto implementa un motor de búsqueda basado en el modelo **TF-IDF (Term Frequency - Inverse Document Frequency)**, permitiendo encontrar artículos relevantes dentro de un reglamento académico.

---

##  Objetivo

Construir un sistema que permita a un estudiante buscar artículos específicos del reglamento (créditos, calendarios, evaluaciones, etc.), priorizando los resultados más relevantes.

---

##  ¿Cómo funciona?

El sistema utiliza el modelo **TF-IDF**, que combina:

- **TF (Term Frequency):** Frecuencia de una palabra en un documento.
- **IDF (Inverse Document Frequency):** Importancia de una palabra en el conjunto de documentos.

###  Fórmula:

\[
TF-IDF = TF \times IDF
\]

---

## ⚙️ Estructura del Proyecto
buscador-tfidf/
│
├── main.py # Ejecución principal
├── tfidf.py # Lógica del modelo TF-IDF
├── dataset.py # Documentos del reglamento
└── README.md



---

## 🚀 Funcionalidades

✔ Cálculo de TF  
✔ Cálculo de IDF  
✔ Cálculo de Score TF-IDF  
✔ Ranking de documentos  
✔ Top 3 documentos más relevantes  
✔ Tabla comparativa de resultados  
✔ Análisis de palabras con mayor y menor IDF  
✔ Normalización de texto (eliminación de tildes)

---

##  Casos de prueba

Se realizaron las siguientes consultas:

-  `creditos academicos`
-  `calendarios academicos`
-  `examenes validacion`

###  Resultado
<img width="1598" height="347" alt="image" src="https://github.com/user-attachments/assets/184d9e76-60f1-44e3-9740-88753c6d830e" />


El sistema logró identificar correctamente los documentos más relevantes en cada caso, generando un ranking basado en la importancia de los términos.




##  Tecnologías utilizadas

- Python 🐍
- NumPy
- Git & GitHub




