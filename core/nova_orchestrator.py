"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

from config.loader import config


class NovaOrchestrator:

    def __init__(
        self,
        brain,
        memory,
        vector_store,
        identity,
        identity_query,
        relationship_engine,
        auto_learner,
        memory_controller,
        event_memory,
        event_extractor,
        event_query,
        agent_router,
        agent
    ):

        self.brain = brain
        self.memory = memory
        self.vector_store = vector_store
        self.identity = identity
        self.identity_query = identity_query
        self.relationship_engine = relationship_engine
        self.auto_learner = auto_learner
        self.memory_controller = memory_controller
        self.event_memory = event_memory
        self.event_extractor = event_extractor
        self.event_query = event_query
        self.agent_router = agent_router
        self.agent = agent

    def _should_use_vector_search(self, text: str) -> bool:

        t = text.strip().lower()

        if len(t) >= 25:
            return True

        if "?" in t:
            return True

        keywords = [
            "hatırla",
            "geçen",
            "önce",
            "daha önce",
            "kim",
            "neydi",
            "nerede",
            "ne zaman",
            "konuşmuştuk"
        ]

        return any(k in t for k in keywords)

    def handle(self, user_input: str):

        # 0 EVENT EXTRACTION
        event = self.event_extractor.extract(user_input)
        if event:
            self.event_memory.add_event(
                event["subject"],
                event["action"],
                event["target"]
            )

        # 1 AUTO LEARN
        learn_result = self.auto_learner.process(user_input)
        if learn_result:
            return learn_result

        # 2 MEMORY CONTROLLER
        control = self.memory_controller.process(user_input)
        if control:
            return control["message"]

        # 3 RELATIONSHIP QUERY
        relation = self.relationship_engine.process(user_input)
        if relation:
            return relation

        # 4 EVENT QUERY
        event_answer = self.event_query.process(user_input)
        if event_answer:
            return event_answer

        # 5 IDENTITY QUERY
        identity_answer = self.identity_query.process(user_input)
        if identity_answer:
            return identity_answer

        # 6 AGENT ROUTER
        tool = self.agent_router.route(user_input)
        if tool:
            result = self.agent.execute(tool)
            if result:
                return result

        # VECTOR MEMORY
        memory_lines = []

        if self._should_use_vector_search(user_input):
            try:
                related = self.vector_store.search(user_input, top_k=2)

                for text, sim in related:
                    memory_lines.append(f"- {text}")

            except Exception:
                pass

        memory_context = "\n".join(memory_lines)

        # SON KONUŞMALAR
        context = self.memory.get_last_messages(6)
        chat_context = "\n".join([f"{r}: {c}" for r, c in reversed(context)])

        # IDENTITY SUMMARY
        identity_context = self.identity.get_summary()

        system_prompt = config.get("system_prompt", "")
        assistant_name = config.get("assistant_name", "Assistant")

        final_prompt = f"""
{system_prompt}

Kimlik:
{identity_context}

İlgili Anılar:
{memory_context}

Son Konuşmalar:
{chat_context}

Kullanıcı Mesajı:
{user_input}

{assistant_name} olarak cevap ver:
""".strip()

        # LLM
        response = self.brain.think(final_prompt)

        # MEMORY SAVE (en sona)
        self.memory.save_message("user", user_input)
        self.memory.save_message("assistant", response)

        return response