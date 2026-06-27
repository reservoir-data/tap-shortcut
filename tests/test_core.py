"""Tests standard tap features using the built-in SDK tests library.

Copyright (c) 2025 Edgar Ramírez-Mondragón
"""

from __future__ import annotations

from singer_sdk.testing import SuiteConfig, get_tap_test_class
from tap_shortcut.tap import TapShortcut

TestTapShortcut = get_tap_test_class(
    TapShortcut,
    suite_config=SuiteConfig(ignore_no_records=True),
)
