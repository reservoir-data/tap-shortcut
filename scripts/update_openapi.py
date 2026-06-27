#!/usr/bin/env python

"""Update the OpenAPI schema from the Shortcut API.

Copyright (c) 2025 Edgar Ramírez-Mondragón
"""

from __future__ import annotations

import http
import http.client
import json
import pathlib
import urllib.request

OPENAPI_URL = "https://developer.shortcut.com/api/rest/v3/shortcut.swagger.json"
PATH = "tap_shortcut/openapi.json"


def main() -> None:
    """Update the OpenAPI schema from the Shortcut API.

    Raises:
        SystemExit: if the request fails.
    """
    path = pathlib.Path(PATH)
    f: http.client.HTTPResponse
    with urllib.request.urlopen(OPENAPI_URL, timeout=5) as f:
        if f.status != http.HTTPStatus.OK:
            msg = f"{(f.status)} Failed to retrieve OpenAPI document: {f.reason}"
            raise SystemExit(msg)

        spec = json.loads(f.read())
        content = json.dumps(spec, indent=2) + "\n"
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
