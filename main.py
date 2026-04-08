from dataset import documentos
from tfidf import calcular_score, calcular_idf_vocabulario

# ======================
# 🔥 1. TABLA IDF
# ======================
idf_scores = calcular_idf_vocabulario(documentos)

print("\n🔝 5 PALABRAS CON MAYOR IDF:")
for palabra, score in idf_scores[:5]:
    print(f"{palabra:<20} {score:.4f}")

print("\n🔻 5 PALABRAS CON MENOR IDF:")
for palabra, score in idf_scores[-5:]:
    print(f"{palabra:<20} {score:.4f}")


# ======================
# 🔥 2. CASOS DE PRUEBA
# ======================
consultas = [
    "creditos academicos",
    "calendarios academicos",
    "examenes validacion"
]

for query in consultas:
    print(f"\n🔎 Consulta: {query}")

    resultados = calcular_score(query, documentos)

    print("\n🏆 TOP 3 DOCUMENTOS:")
    for doc_id, doc, score in resultados[:3]:
        print(f"Doc {doc_id} | Score: {score:.4f}")
        print(f"{doc}\n")


# ======================
# 🔥 3. TABLA COMPARATIVA
# ======================
print("\n📊 TABLA COMPARATIVA DE SCORES")

for query in consultas:
    print(f"\nConsulta: {query}")
    resultados = calcular_score(query, documentos)

    print(f"{'Doc':<5} {'Score':<10}")
    for doc_id, _, score in resultados:
        print(f"{doc_id:<5} {score:.4f}")