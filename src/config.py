from dataclasses import dataclass, field
from typing import List, Optional, Tuple

@dataclass
class TokenSelectionConfig:
    global_keep_ratio: float = 0.5
    full_shot_threshold: float = 0.8
    score_aggregation: str = "mean"
    use_scaling: bool = True
    cache_derope_k: bool = True
    reuse_selection_in_probe: bool = True
    verbose: bool = False
    save_selection_details: bool = False

@dataclass
class MilestoneConfig:
    init_batch: int = 32
    expand_batch: int = 32
    expand_threshold: float = 0.9
    max_capacity: int = 128

@dataclass
class AdaShotConfig:
    window_size: int = 4
    entropy_threshold: float = 0.6
    max_probe_rounds: int = 64
    gen_tokens: int = 2048
    enable_token_selection: bool = True
    token_selection: TokenSelectionConfig = field(default_factory=TokenSelectionConfig)
    milestone: MilestoneConfig = field(default_factory=MilestoneConfig)

def get_format_labels(task_type: str) -> Tuple[str, str]:
    labels = {
        "qa": ("Question", "Answer"),
        "math": ("Problem", "Solution"),
        "summary": ("Article", "Summary"),
        "translation": ("Source", "Translation"),
        "tcm_translation": ("术语", "翻译"),
        "code": ("Task", "Code"),
    }
    return labels.get(task_type, ("Input", "Output"))
