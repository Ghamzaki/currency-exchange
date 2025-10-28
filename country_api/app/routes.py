from fastapi import APIRouter, HTTPException
from app.database import get_connection
import requests
from app.services import fetch_and_store_countries

router = APIRouter()

# Base API endpoint
@router.get("/countries")
def get_countries():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM countries")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

@router.get("/countries/{country_id}")
def get_country(country_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM countries WHERE id = %s", (country_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="Country not found")
    return result

@router.post("/countries")
def create_country(country: dict):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO countries (name, capital, region, population, flag, currency_code)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        country.get("name"),
        country.get("capital"),
        country.get("region"),
        country.get("population"),
        country.get("flag"),
        country.get("currency_code")
    )
    cursor.execute(sql, values)
    conn.commit()
    country_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return {"message": "Country added", "id": country_id}

@router.put("/countries/{country_id}")
def update_country(country_id: int, country: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM countries WHERE id = %s", (country_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Country not found")
    
    sql = """
        UPDATE countries SET name=%s, capital=%s, region=%s, population=%s, flag=%s, currency_code=%s
        WHERE id=%s
    """
    values = (
        country.get("name"),
        country.get("capital"),
        country.get("region"),
        country.get("population"),
        country.get("flag"),
        country.get("currency_code"),
        country_id
    )
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Country updated"}

@router.delete("/countries/{country_id}")
def delete_country(country_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM countries WHERE id = %s", (country_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Country deleted"}

@router.post("/fetch-countries")
def fetch_countries():
    result = fetch_and_store_countries()
    return result