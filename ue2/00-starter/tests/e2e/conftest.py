"""Fixtures fuer echte Browser-Tests gegen einen laufenden FastAPI-Server."""

from __future__ import annotations

import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.request
from collections.abc import Iterator
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).parents[2]


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    """Playwright mit dem unter Manjaro installierten Chromium starten."""
    executable = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH")
    executable = executable or shutil.which("chromium")
    if executable is None:
        pytest.fail(
            "Chromium wurde nicht gefunden. Unter Manjaro: "
            "sudo pacman -S chromium"
        )

    return {**browser_type_launch_args, "executable_path": executable}


@pytest.fixture
def live_server() -> Iterator[str]:
    """Pro Test einen isolierten Server mit frischen In-Memory-Daten starten."""
    port = _free_port()
    base_url = f"http://127.0.0.1:{port}"
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
        ],
        cwd=PROJECT_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )

    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        if process.poll() is not None:
            stderr = process.stderr.read() if process.stderr else ""
            pytest.fail(f"FastAPI-Server konnte nicht starten:\n{stderr}")
        try:
            with urllib.request.urlopen(f"{base_url}/health", timeout=0.2):
                break
        except OSError:
            time.sleep(0.05)
    else:
        process.terminate()
        process.wait(timeout=5)
        pytest.fail("FastAPI-Server war nach 10 Sekunden nicht erreichbar")

    try:
        yield base_url
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
