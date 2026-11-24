from typing import Annotated
from pydantic import BaseModel, ConfigDict, StringConstraints, StrictBool, model_validator

Title = Annotated[str, StringConstraints(strict=True, min_length=1, max_length=200, pattern=r'\S')]

class TodoReplace(BaseModel):
    model_config = ConfigDict(extra='forbid')
    title: Title
    completed: StrictBool

class TodoCreate(TodoReplace):
    completed: StrictBool = False

class Todo(TodoReplace):
    id: int

class TodoUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    title: Title | None = None
    completed: StrictBool | None = None

    @model_validator(mode='after')
    def reject_null(self):
        if any(getattr(self, key) is None for key in self.model_fields_set):
            raise ValueError('null ist nicht erlaubt')
        return self
