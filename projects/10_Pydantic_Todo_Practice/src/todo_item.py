from datetime import datetime

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100, description="任务标题")
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now, description="任务创建时间")
