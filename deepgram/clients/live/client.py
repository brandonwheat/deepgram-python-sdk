# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

from .v1.client import LiveClient as LiveClientLatest
from .v1.legacy_client import LegacyLiveClient as LegacyLiveClientLatest
from .v1.options import LiveOptions as LiveOptionsLatest

'''
The client.py points to the current supported version in the SDK.
Older versions are supported in the SDK for backwards compatibility.
'''
class LiveOptions(LiveOptionsLatest):
  pass

class LiveClient(LiveClientLatest):
  """
    Please see LiveClientLatest for details
    """
  def __init__(self, config):
      super().__init__(config)

class LegacyLiveClient(LegacyLiveClientLatest):
  """
    Please see LiveClientLatest for details
    """
  def __init__(self, config):
      super().__init__(config)
  