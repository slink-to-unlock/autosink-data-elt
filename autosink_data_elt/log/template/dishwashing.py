# 내장
from typing import List, Deque
from dataclasses import dataclass, field
from collections import deque

# 프로젝트
from autosink_data_elt.log.template.interaction import *


@dataclass
class DishwashingDataV1:
    version: int
    user_id: str
    dishwashing_id: str
    dishwashing_start: str
    interaction: List[InteractionV1] = field(default_factory=list)


@dataclass
class DishwashingDataV2:
    version: int
    user_id: str
    dishwashing_id: str
    dishwashing_start: str
    interaction: Deque[InteractionV1] = field(default_factory=deque)
