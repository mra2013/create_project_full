from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# In-memory database for demonstration purposes
cases_db = []

class Case:
    def __init__(self, case_id: int, title: str, description: str):
        self.case_id = case_id
        self.title = title
        self.description = description

@router.post("/cases/", response_model=Case)
async def create_case(case: Case):
    cases_db.append(case)
    return case

@router.get("/cases/{case_id}", response_model=Case)
async def read_case(case_id: int):
    for case in cases_db:
        if case.case_id == case_id:
            return case
    raise HTTPException(status_code=404, detail="Case not found")

@router.put("/cases/{case_id}", response_model=Case)
async def update_case(case_id: int, updated_case: Case):
    for index, case in enumerate(cases_db):
        if case.case_id == case_id:
            cases_db[index] = updated_case
            return updated_case
    raise HTTPException(status_code=404, detail="Case not found")

@router.delete("/cases/{case_id}", response_model=dict)
async def delete_case(case_id: int):
    for index, case in enumerate(cases_db):
        if case.case_id == case_id:
            del cases_db[index]
            return {"message": "Case deleted successfully"}
    raise HTTPException(status_code=404, detail="Case not found")

@router.get("/cases/", response_model=List[Case])
async def list_cases():
    return cases_db
