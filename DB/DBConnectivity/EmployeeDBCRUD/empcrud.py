import pymysql

class EmployeeDB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="pass@word1",
                database="employeedb"
            )
            self.cursor = self.conn.cursor()
            print("Database connection established!")
        except pymysql.MySQLError as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    # CREATE - Using 'eid' and 'ename' from your schema
    def create_employee(self, eid, ename, salary, bonus=0.0):
        try:
            self.cursor.execute(
                "INSERT INTO employee (eid, ename, salary, bonus) VALUES (%s, %s, %s, %s)",
                (eid, ename, salary, bonus)
            )
            self.conn.commit()
            print(f"Employee '{ename}' created successfully.")
        except pymysql.MySQLError as e:
            print(f"Error creating employee: {e}")

    # READ
    def read_employees(self):
        try:
            self.cursor.execute("SELECT * FROM employee")
            rows = self.cursor.fetchall()
            if not rows:
                print("No employees found.")
            for row in rows:
                print(row)
        except pymysql.MySQLError as e:
            print(f"Error reading employees: {e}")

    # UPDATE - Using 'eid' as the primary key
    def update_employee(self, eid, new_salary):
        try:
            self.cursor.execute(
                "UPDATE employee SET salary=%s WHERE eid=%s",
                (new_salary, eid)
            )
            self.conn.commit()
            print(f"Employee ID {eid} updated successfully.")
        except pymysql.MySQLError as e:
            print(f"Error updating employee: {e}")

    # DELETE
    def delete_employee(self, eid):
        try:
            self.cursor.execute(
                "DELETE FROM employee WHERE eid=%s",
                (eid,)
            )
            self.conn.commit()
            print(f"Employee ID {eid} deleted successfully.")
        except pymysql.MySQLError as e:
            print(f"Error deleting employee: {e}")

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    db = EmployeeDB()

    # Match your schema: (eid, ename, salary, bonus)
    db.create_employee(101, "Alice", 50000.0, 500.0)
    db.create_employee(102, "Bob", 55000.0, 600.0)

    print("\nAll Employees:")
    db.read_employees()

    db.update_employee(101, 62000.0)
    db.delete_employee(102)

    db.close()