# 내장
from typing import List
from dataclasses import dataclass, field

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
    interaction: List[InteractionV2] = field(default_factory=list)
