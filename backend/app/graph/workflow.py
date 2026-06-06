from langgraph.graph import StateGraph

from app.graph.state import AgentState

from app.agents.query_agent import query_agent
from app.agents.search_agent import search_agent
from app.agents.validation_agent import validation_agent
from app.agents.summary_agent import summary_agent
from app.agents.citation_agent import citation_agent
from app.agents.response_agent import response_agent
from app.agents.memory_agent import memory_agent




workflow = StateGraph(AgentState)

workflow.add_node(
    "query",
    query_agent
)

workflow.add_node(
    "memory",
    memory_agent
)

workflow.add_node(
    "search",
    search_agent
)

workflow.add_node(
    "validate",
    validation_agent
)

workflow.add_node(
    "summary",
    summary_agent
)

workflow.add_node(
    "citation",
    citation_agent
)

workflow.add_node(
    "response",
    response_agent
)

# edges 

workflow.set_entry_point(
    "query"
)

workflow.add_edge(
    "query",
    "memory"
)

workflow.add_edge(
    "memory",
    "search"
)

workflow.add_edge(
    "search",
    "validate"
)

workflow.add_edge(
    "validate",
    "citation"
)

workflow.add_edge(
    "citation",
    "response"
)

graph = workflow.compile()