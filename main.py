from fastapi import FastAPI, HTTPException
from typing import List, Optional
import json
import random
from pathlib import Path

app = FastAPI(title="Quotes API",
              description="An API for managing and generating quotes")


def load_quotes() -> List[dict]:
    quotes_file = Path("quotes.json")
    if not quotes_file.exists():
        return []
    with open(quotes_file, "r") as f:
        return json.load(f)


quotes_data = load_quotes()['quotes']


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Quotes API"}


@app.get("/quotes", response_model=List[dict])
async def get_all_quotes():
    """Get all available quotes."""
    return quotes_data


@app.get("/quotes/random")
async def get_random_quote():
    """Get a random quote."""
    if not quotes_data:
        raise HTTPException(status_code=404, detail="No quotes available")
    return random.choice(quotes_data)


@app.get("/quotes/search")
async def search_quotes(author: Optional[str] = None,
                        keyword: Optional[str] = None):
    """Search quotes by author or keyword."""
    results = quotes_data

    if author:
        results = [q for q in results if author.lower() in q["author"].lower()]

    if keyword:
        results = [q for q in results if keyword.lower() in q["text"].lower()]

    if not results:
        raise HTTPException(status_code=404,
                            detail="No quotes found matching criteria")

    return results
