from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/works",
    tags=["works"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

fake_works_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_works():
    return fake_works_db


@router.get("/{works_id}")
async def read_item(works_id: str):
    if works_id not in fake_works_db:
        raise HTTPException(status_code=404, detail="works Item not found")
    return {"name": fake_works_db[works_id]["name"], "works_id": works_id}


@router.put(
    "/{works_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(works_id: str):
    if works_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"works_id": works_id, "name": "The great Plumbus"}