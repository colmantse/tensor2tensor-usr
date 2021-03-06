# coding=utf-8
"""Additional hparams for standard T2T models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.utils import registry
from tensor2tensor.models.transformer import transformer_base


@registry.register_hparams
def transformer_base_12gb_gpu():
  """HParams for transformer base model for a single 12GB gpu."""
  hparams = transformer_base()
  hparams.learning_rate_warmup_steps = 8000
  hparams.batch_size = 8192
  return hparams


@registry.register_hparams
def transformer_base_12gb_gpu_large_batch():
  """Replication of Vaswani et al., 2017 on a single 12GB gpu.
  
  Requires the T2T fork from https://github.com/fstahlberg/tensor2tensor
  """
  hparams = transformer_base()
  hparams.batch_size = 8192
  hparams.fake_gpu_multiplier = 4
  hparams.optimizer = "LargebatchAdam"
  return hparams
