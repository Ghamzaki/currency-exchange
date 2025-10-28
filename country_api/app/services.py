import requests
from app.database import get_connection
from requests.exceptions import RequestException
import logging
from mysql.connector import Error

logger = logging.getLogger(__name__)

def fetch_and_store_countries():
    url = "https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
    except RequestException as e:
        logger.error(f"Error fetching countries from external API: {e}")
        return {"message": f"Error fetching countries: {e}"}

    conn = get_connection()
    if conn is None:
        logger.error("Failed to get database connection.")
        return {"message": "Failed to connect to database."}

    cursor = conn.cursor()

    for country in data:
        name = country.get("name")
        capital = country.get("capital")
        region = country.get("region")
        population = country.get("population")
        flag = country.get("flag")
        currencies = country.get("currencies", [])
        currency_code = currencies[0].get("code") if currencies and isinstance(currencies, list) and len(currencies) > 0 and isinstance(currencies[0], dict) else None

        sql = """
        INSERT INTO countries (name, capital, region, population, flag, currency_code)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE name=VALUES(name)
        """
        try:
            cursor.execute(sql, (name, capital, region, population, flag, currency_code))
        except Error as e:
            logger.error(f"Error inserting/updating country {name}: {e}")
            conn.rollback() # Rollback in case of error
            return {"message": f"Error storing country {name}: {e}"}

    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Countries fetched and stored successfully!"}