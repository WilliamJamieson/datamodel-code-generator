# generated by datamodel-codegen:
#   filename:  test.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from pydantic import BaseModel, Field

from . import base_test


class Model(BaseModel):
    test_id: str = Field(..., description='test ID')
    test_ip: base_test.First
