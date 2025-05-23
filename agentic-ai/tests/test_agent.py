import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools import echo_tool


def test_echo_tool():
    assert echo_tool("say something") == "Echo: say something"

