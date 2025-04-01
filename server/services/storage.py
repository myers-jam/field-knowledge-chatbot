
import numpy as np

stored_embeddings = []

def save_embedding(doc_name, text, vector):
    stored_embeddings.append({
        "doc": doc_name,
        "text": text,
        "vector": vector
    })

def find_similar_chunks(query_vector, top_k=3):
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    similarities = [
        {
            "score": cosine_similarity(query_vector, entry["vector"]),
            "text": entry["text"],
            "doc": entry["doc"]
        }
        for entry in stored_embeddings
    ]

    return sorted(similarities, key=lambda x: x["score"], reverse=True)[:top_k]
