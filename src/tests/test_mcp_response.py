import pytest
from models.response import MCPResponse


def test_without_error():
    model = MCPResponse(result={}, error=None)
    assert model.result == {}
    assert model.error == None

def test_with_error():
    model = MCPResponse(result=None, error="Error")
    assert model.result == None
    assert model.error == "Error"
