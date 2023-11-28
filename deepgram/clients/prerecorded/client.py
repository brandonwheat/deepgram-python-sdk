# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

from .v1.client import PreRecordedClient as PreRecordedClientLatest
from .v1.options import PrerecordedOptions as PrerecordedOptionsLatest
from .source import PrerecordedSource, FileSource, UrlSource

'''
The client.py points to the current supported version in the SDK.
Older versions are supported in the SDK for backwards compatibility.
'''
class PrerecordedOptions(PrerecordedOptionsLatest):
    pass

class PreRecordedClient(PreRecordedClientLatest):
    """
    Please see PreRecordedClientLatest for details
    """
    def __init__(self, config):
        self.config = config
        super().__init__(config)