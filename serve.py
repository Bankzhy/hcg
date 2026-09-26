#!/usr/bin/env python3
"""Serve the compiled HCG Web client on the local loopback interface."""

from __future__ import annotations

import argparse
import http.server
import os
from pathlib import Path
import socket
import threading
from urllib.parse import urlsplit
import webbrowser


BASE_PATH = "/hcg"


class HcgRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Static handler with Flutter base-path mapping and SPA fallback."""

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def translate_path(self, path: str) -> str:
        request_path = urlsplit(path).path
        if request_path == BASE_PATH:
            request_path = f"{BASE_PATH}/"
        if request_path.startswith(f"{BASE_PATH}/"):
            request_path = request_path[len(BASE_PATH) :]
        return super().translate_path(request_path)

    def send_head(self):  # type: ignore[no-untyped-def]
        requested = self.translate_path(self.path)
        if self.path not in ("/", f"{BASE_PATH}/") and not os.path.exists(requested):
            self.path = "/index.html"
        return super().send_head()


class HcgServer(http.server.ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def available_port(preferred: int) -> int:
    for port in range(preferred, preferred + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            try:
                probe.bind(("127.0.0.1", port))
            except OSError:
                continue
            return port
    raise RuntimeError("No available local port was found")


def main() -> None:
    parser = argparse.ArgumentParser(description="Start HCG locally")
    parser.add_argument("--port", type=int, default=4173)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    package_dir = Path(__file__).resolve().parent
    if not (package_dir / "index.html").is_file():
        raise SystemExit("HCG Web files are missing next to serve.py")

    port = available_port(args.port)
    handler = lambda *handler_args, **handler_kwargs: HcgRequestHandler(
        *handler_args,
        directory=str(package_dir),
        **handler_kwargs,
    )
    server = HcgServer(("127.0.0.1", port), handler)
    url = f"http://127.0.0.1:{port}{BASE_PATH}/"

    print(f"HCG is running at {url}")
    print("Press Ctrl+C to stop.")
    if not args.no_browser:
        threading.Timer(0.35, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping HCG...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
