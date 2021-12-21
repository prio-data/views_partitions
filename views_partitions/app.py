
from typing import List
import views_schema
from fastapi import FastAPI

app = FastAPI()


@app.get("/partitions/")
def list_partitions() -> List[views_schema.partitioning.Partitions]:
    pass
