import mysql.connector 
def get_connection():
    try:
        conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='*52206153Rg',
        database='school'
        )
        
        return conn
    
    except Exception as e:
        print("--Failed to connect to database: ", e)

def execute_query(sql,values=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if values is not None:
            cursor.execute(sql,values)
        else:
            cursor.execute(sql)

        if sql.strip().lower().startswith("select"):
            return cursor.fetchall()
        else:
            conn.commit()
    except Exception as e:
        print("Failed to run the query: ",e)
    
    finally:
        if "cursor" in locals(): 
            cursor.close()
        if "conn" in locals():
            conn.close()
