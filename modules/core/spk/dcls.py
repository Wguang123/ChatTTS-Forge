from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass(repr=False, eq=False)
class DcSpkMeta:
    name: str = ""
    desc: str = ""
    gender: str = "*"

    author: str = ""
    version: str = ""


# embedding
@dataclass(repr=False, eq=False)
class DcSpkVoiceToken:
    model_id: str
    model_hash: str

    # 可以填入特殊 token 或者 tensor
    # 一般都是 tensor
    # egs: ["<EMOTION_START>","xxx","<EMOTION_END>", [...<torch.Tensor>...]]
    tokens: list[Union[str, list]]


@dataclass(repr=False, eq=False)
class DcSpkSample:
    wav: bytes
    text: str


@dataclass(repr=False, eq=False)
class DcSpkReference:
    text: Optional[str] = None

    wav: Optional[bytes] = None
    wav_sr: Optional[int] = None

    # 标注情绪
    emotion: Optional[str] = None


@dataclass(repr=False, eq=False)
class DcSpkTrainInfo:
    steps: int
    epochs: int
    dataset: str
    samples: int
    batch_size: int
    optimizer: str
    lr: float
    loss: str

    extra: Optional[dict]


# 这个说话人的推荐配置
@dataclass(repr=False, eq=False)
class DcSpkInferConfig:
    tempature: float
    top_k: int
    top_p: float
    max_tokens: int
    repetition_penalty: float

    # 应该没几个模型支持这个...
    emotion: str


@dataclass(repr=False, eq=False)
class DcSpk:
    id: str
    version: str = "0.1"

    meta: DcSpkMeta = field(default_factory=DcSpkMeta)
    token: List[DcSpkVoiceToken] = field(default_factory=list)
    samples: List[DcSpkSample] = field(default_factory=list)
    refs: List[DcSpkReference] = field(default_factory=list)
    train_info: Optional[DcSpkTrainInfo] = None

    recommend_config: Optional[DcSpkInferConfig] = None
