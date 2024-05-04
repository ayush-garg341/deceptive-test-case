import unittest
import mysql.connector


class TestDBOperations(unittest.TestCase):

    def test_insert_data(self):
        connection = mysql.connector.connect(
            user="admin",
            password="admin123",
            host="localhost",
            database="test",
            port=3315,
        )
        cursor = connection.cursor()
        cursor.execute("Use test")
        cursor.execute("SELECT @@GLOBAL.transaction_ISOLATION")
        print(type(connection))
        print(connection._autocommit)
        rows = cursor.fetchall()
        print(rows)
        cursor.execute(
            "CREATE TABLE test (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), section varchar(5), active varchar(10))"
        )
        query = "INSERT INTO test (name, section, active) VALUES (%s, %s, %s)"
        data = [
            ("Ayush", "C", "1"),
            ("Jack", "D", "1"),
            ("Joe", "E", "1"),
            ("William", "F", "1"),
        ]
        cursor.executemany(query, data)
        print(cursor.rowcount)
        # update.connection.commit()
        update_query = "UPDATE {0} SET active=0 WHERE section = %(section)s".format(
            "test"
        )
        data_to_be_updated = [
            {"section": "C"},
            {"section": "D"},
            {"section": "E"},
            {"section": "F"},
        ]
        cursor.executemany(update_query, data_to_be_updated)
        print(cursor.rowcount)
        # update.connection.commit()
        query = "SELECT * FROM test"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)

        cursor.execute("DROP table test")
        cursor.close()
        connection.close()


if __name__ == "__main__":
    unittest.main()
