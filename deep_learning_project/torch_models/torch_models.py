"""
基于原生torch对于模型的定义。

基础依然是基于torch.nn.Module定义的模型，分离设计以实现与具体训练器的低耦合。

约定:
    - 在这个位置的是整体模型，为实验需求需要易于变动。
"""

from __future__ import annotations

# from .torch_modules import (
#
# )

import torch

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class DemoModel(torch.nn.Module):
    def __init__(
        self,
        torch_model_config: dict,
    ):
        super().__init__()
        self.self_attention_layer = torch.nn.MultiheadAttention(
            embed_dim=torch_model_config['embed_dim'],
            num_heads=torch_model_config['num_heads'],
            batch_first=True,
        )
        self.ffn_layer = torch.nn.Sequential(
            torch.nn.Linear(
                in_features=torch_model_config['embed_dim'],
                out_features=torch_model_config['ffn_embed_dim']
            ),
            torch.nn.ReLU(),
            torch.nn.Linear(
                in_features=torch_model_config['ffn_embed_dim'],
                out_features=1,
            ),
        )

    def forward(
        self,
        inputs: torch.Tensor,
    ) -> torch.Tensor:
        attention_outputs, attention_score = self.self_attention_layer(
            inputs, inputs, inputs
        )
        outputs = self.ffn_layer(attention_outputs)
        return outputs

