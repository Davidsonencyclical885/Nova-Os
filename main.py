"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""

from core.brain import Brain
from core.nova_orchestrator import NovaOrchestrator

from memory.database import MemoryDB
from memory.vector_store import VectorStore

from identity.identity_engine import IdentityEngine
from identity.identity_query_engine import IdentityQueryEngine
from identity.relationship_query_engine import RelationshipQueryEngine
from identity.auto_learn import AutoLearner

from memory.memory_controller import MemoryController
from memory.event_memory import EventMemory
from memory.event_extractor import EventExtractor
from memory.event_query_engine import EventQueryEngine

from core.llm_agent_router import LLMAgentRouter
from core.agent_planner import AgentPlanner


brain = Brain()
memory = MemoryDB()
vector_store = VectorStore()

identity = IdentityEngine()
identity_query = IdentityQueryEngine(identity)
relationship_engine = RelationshipQueryEngine()

auto_learner = AutoLearner(identity)
memory_controller = MemoryController(identity)

event_memory = EventMemory()
event_extractor = EventExtractor()
event_query = EventQueryEngine(event_memory)

agent_router = LLMAgentRouter(brain)
agent = AgentPlanner()

orchestrator = NovaOrchestrator(
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
)

from config.loader import config

username = config.get("user_name", "User")

print("NOVA OS başlatıldı.")

while True:
    user_input = input(f"{username} > ").strip()

    if not user_input:
        continue

    response = orchestrator.handle(user_input)

    print("Nova >", response)