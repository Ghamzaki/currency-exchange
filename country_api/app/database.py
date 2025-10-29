import mysql.connector
from mysql.connector import Error
from app.config import settings
import logging

logger = logging.getLogger(__name__)

def create_table():
    conn = get_connection()
    if conn is None:
        logger.error("Failed to get database connection for table creation.")
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            capital VARCHAR(200),
            region VARCHAR(100),
            population BIGINT,
            flag VARCHAR(500),
            currency_code VARCHAR(10)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    logger.info("✅ Table 'countries' created successfully.")

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME,
            port=int(settings.DB_PORT) if settings.DB_PORT else 3306
        )
        if connection.is_connected():
            logger.info("Connected to MySQL successfully.")
        return connection
    except Error as e:
        logger.error(f"Error connecting to MySQL: {e}")
        return None
