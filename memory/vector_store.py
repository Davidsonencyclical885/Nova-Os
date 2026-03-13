"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import faiss
import numpy as np
import sqlite3
import requests
import os
from config.paths import DB_PATH, FAISS_INDEX_PATH

class VectorStore:

    def __init__(self):

        self.dim = 768
        self.index_file = FAISS_INDEX_PATH
        os.makedirs(os.path.dirname(self.index_file), exist_ok=True)

        # FAISS index yükle veya oluştur
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
        else:
            self.index = faiss.IndexFlatL2(self.dim)

        # SQLite bağlantı
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vector_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
        """)

        self.conn.commit()

    def embed(self, text):

        try:
            response = requests.post(
                "http://localhost:11434/api/embeddings",
                json={
                    "model": "nomic-embed-text",
                    "prompt": text
                }
            )

            emb = response.json()["embedding"]

            return np.array(emb, dtype="float32")

        except Exception as e:
            print("Embedding error:", e)
            return np.zeros(self.dim).astype("float32")

    def add(self, text):

        vector = self.embed(text)

        # FAISS'e ekle
        self.index.add(np.array([vector]))

        # SQLite kaydı
        self.cursor.execute(
            "INSERT INTO vector_memory (text) VALUES (?)",
            (text,)
        )

        self.conn.commit()

        # INDEX DISKE YAZ
        faiss.write_index(self.index, self.index_file)

    def search(self, query, top_k=3):

        query_vector = self.embed(query)

        D, I = self.index.search(np.array([query_vector]), top_k)

        results = []

        for pos, idx in enumerate(I[0]):

            if idx == -1:
                continue

            self.cursor.execute(
                "SELECT text FROM vector_memory WHERE id=?",
                (idx + 1,)
            )

            row = self.cursor.fetchone()

            if row:
                similarity = float(D[0][pos])
                results.append((row[0], similarity))

        return results