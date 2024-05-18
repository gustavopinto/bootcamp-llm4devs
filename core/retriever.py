from pgvector.psycopg2 import register_vector
import psycopg2
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

def database_params():
    return {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT")
    }

def test_connection():
    try:
        connection = psycopg2.connect(**database_params())
        cursor = connection.cursor()

        cursor.execute("SELECT 1")

        result = cursor.fetchone()
        print("Conexão com banco bem-sucedida? ", result[0] == 1)
        return result[0]

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar:", error)
    finally:
        # Fechar cursor e conexão
        if connection:
            cursor.close()
            connection.close()

def store(content, embeddings):
    for i in range(len(content)):
        _store(content[i], embeddings[i])

def _store(content, embeddings):
    try:
        conn = psycopg2.connect(**database_params())
        register_vector(conn)
        cur = conn.cursor()

        cur.execute("INSERT INTO embeddings (content, chars, embeddings) VALUES (%s, %s, %s);", (content, len(content), embeddings))

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar:", error)
    finally:
        if conn:
            cur.close()
            conn.commit()
            conn.close()
            

def retrieve(embeddings):
    try:
        conn = psycopg2.connect(**database_params())
        register_vector(conn)
        cur = conn.cursor()
        embeddings = np.array(embeddings)
        
        cur.execute("""
                    SELECT content
                    FROM embeddings 
                    ORDER BY embeddings <=> %s 
                    LIMIT 3""", (embeddings,))
        
        return cur.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar:", error)
    finally:
        if conn:
            cur.close()
            conn.close()