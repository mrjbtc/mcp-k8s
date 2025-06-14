import pytest
from models.response import MCPResponse


def test_without_error():
    model = MCPResponse(result={}, error=None)
    assert model.result == {}
    assert model.error == None
