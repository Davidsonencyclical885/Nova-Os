"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

import re


class InformationExtractor:

    def extract(self, text: str):

        t = text.lower()

        result = {
            "person": None,
            "relation": None,
            "age": None,
            "school": None,
            "grade": None
        }

        # -----------------
        # AGE
        # -----------------

        age_match = re.search(r"\b(\d{1,3})\s*yaşında\b", t)

        if age_match:
            result["age"] = int(age_match.group(1))

        # -----------------
        # SCHOOL LEVEL
        # -----------------

        if "ilkokul" in t:
            result["school"] = "ilkokul"

        elif "ortaokul" in t:
            result["school"] = "ortaokul"

        elif "lise" in t:
            result["school"] = "lise"

        elif "üniversite" in t or "universite" in t:
            result["school"] = "üniversite"

        # -----------------
        # GRADE (3. sınıf gibi)
        # -----------------

        grade_match = re.search(r"(\d{1,2})\.?\s*sınıf", t)

        if grade_match:
            result["grade"] = int(grade_match.group(1))

        # -----------------
        # RELATION
        # -----------------

        relations = [
            "kardeşim",
            "arkadaşım",
            "sevgilim",
            "kız arkadaşım",
            "eski sevgilim",
            "dostum",
            "tanıdığım",
            "değerlim"
        ]

        for r in relations:
            if r in t:
                result["relation"] = r
                break

        # -----------------
        # PERSON NAME
        # -----------------

        words = t.split()

        # relation kelimesinden önceki kelimeyi isim kabul et
        if result["relation"]:

            rel_word = result["relation"].split()[0]

            rel_index = None

            for i, w in enumerate(words):
                if rel_word in w:
                    rel_index = i
                    break

            if rel_index is not None and rel_index > 0:

                candidate = words[rel_index - 1]

                if len(candidate) > 2:
                    result["person"] = candidate.title()

        # fallback: ilk kelimeyi isim kabul et
        if not result["person"] and len(words) > 0:

            candidate = words[0]

            if candidate not in [
                "benim",
                "ve",
                "ile",
                "bir",
                "bu"
            ]:
                result["person"] = candidate.title()

        # -----------------

        if not any(result.values()):
            return None

        return result