from sqlalchemy.orm import mapped_column
from sqlalchemy import text
from typing import Annotated
import datetime


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))]