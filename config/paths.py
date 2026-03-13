"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUNTIME_DIR = os.path.join(BASE_DIR, "runtime")

MEMORY_DIR = os.path.join(RUNTIME_DIR, "memory")
IDENTITY_DIR = os.path.join(RUNTIME_DIR, "identity")

DB_PATH = os.path.join(MEMORY_DIR, "memory.db")
FAISS_INDEX_PATH = os.path.join(MEMORY_DIR, "nova_memory.index")

KNOWLEDGE_GRAPH_PATH = os.path.join(IDENTITY_DIR, "knowledge_graph.json")
PEOPLE_GRAPH_PATH = os.path.join(IDENTITY_DIR, "people_graph.json")