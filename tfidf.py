import numpy as np
import unicodedata

# ----------------------
# LIMPIAR TEXTO (QUITAR TILDES)
# ----------------------
def limpiar_texto(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto


# ----------------------
# TF
# ----------------------
def calcular_tf(termino, documento):
    documento = limpiar_texto(documento)
    termino = limpiar_texto(termino)

    palabras = documento.split()
    return palabras.count(termino) / len(palabras)


# ----------------------
# IDF
# ----------------------
def calcular_idf(termino, documentos):
    termino = limpiar_texto(termino)

    N = len(documentos)
    df = sum(1 for doc in documentos if termino in limpiar_texto(doc))

    return np.log(N / df) if df > 0 else 0


# ----------------------
# SCORE TF-IDF
# ----------------------
def calcular_score(query, documentos):
    resultados = []

    query = limpiar_texto(query)

    for i, doc in enumerate(documentos):
        score = 0
        palabras_query = query.split()

        for termino in palabras_query:
            tf = calcular_tf(termino, doc)
            idf = calcular_idf(termino, documentos)
            score += tf * idf

        resultados.append((i+1, doc, score))

    resultados.sort(key=lambda x: x[2], reverse=True)
    return resultados


# ----------------------
# VOCABULARIO
# ----------------------
def obtener_vocabulario(documentos):
    vocab = set()
    for doc in documentos:
        limpio = limpiar_texto(doc)
        for palabra in limpio.split():
            vocab.add(palabra)
    return vocab


# ----------------------
# IDF DE TODAS LAS PALABRAS
# ----------------------
def calcular_idf_vocabulario(documentos):
    vocab = obtener_vocabulario(documentos)
    idf_scores = []

    for palabra in vocab:
        idf = calcular_idf(palabra, documentos)
        idf_scores.append((palabra, idf))

    return sorted(idf_scores, key=lambda x: x[1], reverse=True)