"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import sqlite3
from datetime import datetime
from config.paths import DB_PATH

class MemoryDB:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        # konuşma geçmişi
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT,
            timestamp TEXT
        )
        """)

        # embedding vektörleri
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            vector TEXT
        )
        """)

        # identity verileri
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS identity (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)

        self.conn.commit()

    def save_message(self, role, content):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO conversations (role,content,timestamp) VALUES (?,?,?)",
            (role, content, datetime.now().isoformat())
        )

        self.conn.commit()

    def get_last_messages(self, limit=6):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT role,content FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,)
        )

        return cursor.fetchall()

