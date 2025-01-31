from ..core import State
from .diagrams import GraphMachine
from .diagrams_base import BaseGraph
from logging import Logger
from typing import Type, Optional, Dict, List, Union, IO, DefaultDict
try:
    from graphviz import Digraph
    from graphviz.dot import SubgraphContext
except ImportError:
    class Digraph:
        pass

    class SubgraphContext:
        pass

_LOGGER: Logger

class Graph(BaseGraph):
    custom_styles: Dict[str, DefaultDict]
    def __init__(self, machine: Type[GraphMachine]) -> None: ...
    def set_previous_transition(self, src: str, dst: str) -> None: ...
    def set_node_style(self, state: str, style: str) -> None: ...
    def reset_styling(self) -> None: ...
    def _add_nodes(self, states: List[Dict[str, str]], container: Union[Digraph, SubgraphContext]) -> None: ...
    def _add_edges(self, transitions: List[Dict[str, str]], container: Union[Digraph, SubgraphContext]) -> None: ...
    def generate(self) -> None: ...
    def get_graph(self, title: Optional[str] = ..., roi_state: Optional[str] = ...) -> Digraph: ...
    @staticmethod
    def draw(self, filename: Optional[str, IO], format:Optional[str] = ...,
             prog: Optional[str] = ..., args:str = ...) -> Optional[str]: ...

class NestedGraph(Graph):
    _cluster_states: List[str]
    def __init__(self, *args, **kwargs) -> None: ...
    def set_previous_transition(self, src: str, dst: str) -> None: ...
    def _add_nodes(self, states: List[Dict[str, str]], container: Union[Digraph, SubgraphContext]) -> None: ...
    def _add_nested_nodes(self, states: List[Dict[str, Union[str, List[Dict[str, str]]]]], container: Union[Digraph, SubgraphContext],
                          prefix: str, default_style: str) -> None: ...
    def _add_edges(self, transitions: List[Dict[str, str]], container: Union[Digraph, SubgraphContext]): ...
    def _create_edge_attr(self, src: str, dst: str, transition: Dict[str, str]): ...

def _filter_states(states: List[Dict[str, str]], state_names: List[str], state_cls: Type[State],
                   prefix: Optional[List[str]] = ...) -> List[Dict[str, str]]: ...
