import requests
import os

API = "http://127.0.0.1:8000"

def pause():
    input("Press Enter to continue...")



def login():
    print("===== LOGIN =====")
    while True:
        u = input("Username: ")
        p = input("Password: ")
        r = requests.post(f"{API}/login", params={"username": u, "password": p}).text

        if "SUCCESS" in r:
            break

        print("Invalid. Try again.")



def add_staff():
    sid = input("Staff ID: ")
    name = input("Name: ")
    dept = input("Dept ID: ")
    pos = input("Position: ")
    sal = input("Salary: ")
    print(requests.post(f"{API}/staff/add",
        params={"staff_id": sid, "name": name, "dept_id": dept, "position": pos, "salary": sal}).text)
    pause()


def update_staff():
    sid = input("Staff ID: ")
    name = input("Name: ")
    dept = input("Dept ID: ")
    pos = input("Position: ")
    sal = input("Salary: ")
    print(requests.post(f"{API}/staff/update",
        params={"staff_id": sid, "name": name, "dept_id": dept, "position": pos, "salary": sal}).text)
    pause()


def delete_staff():
    sid = input("Staff ID: ")
    print(requests.post(f"{API}/staff/delete", params={"staff_id": sid}).text)
    pause()


def list_staff():
    print(requests.get(f"{API}/staff/list").text)
    pause()


def search_staff():
    name = input("Enter name: ")
    print(requests.get(f"{API}/staff/search", params={"name": name}).text)
    pause()


def adjust_salary():
    sid = input("Staff ID: ")
    amt = float(input("Change (+/-): "))
    print(requests.post(f"{API}/staff/adjust_salary", params={"staff_id": sid, "change": amt}).text)
    pause()


def promote_staff():
    sid = input("Staff ID: ")
    pos = input("New Position: ")
    print(requests.post(f"{API}/staff/promote", params={"staff_id": sid, "new_position": pos}).text)
    pause()



def add_dept():
    did = input("Dept ID: ")
    name = input("Dept Name: ")
    print(requests.post(f"{API}/department/add", params={"dept_id": did, "name": name}).text)
    pause()


def update_dept():
    did = input("Dept ID: ")
    name = input("New Dept Name: ")
    print(requests.post(f"{API}/department/update", params={"dept_id": did, "name": name}).text)
    pause()


def delete_dept():
    did = input("Dept ID: ")
    print(requests.post(f"{API}/department/delete", params={"dept_id": did}).text)
    pause()


def list_dept():
    print(requests.get(f"{API}/department/list").text)
    pause()



def add_attendance():
    sid = input("Staff ID: ")
    date = input("Date (YYYY-MM-DD): ")
    status = input("Present/Absent: ")
    print(requests.post(f"{API}/attendance/add",
        params={"staff_id": sid, "date": date, "status": status}).text)
    pause()


def view_attendance():
    sid = input("Staff ID: ")
    print(requests.get(f"{API}/attendance/summary", params={"staff_id": sid}).text)
    pause()


def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("StaffManager Pro with API and File Support")
    print("1. Add Staff")
    print("2. Update Staff")
    print("3. Delete Staff")
    print("4. List Staff")
    print("5. Add Department")
    print("6. Update Department")
    print("7. Delete Department")
    print("8. List Department")
    print("9. Adjust Staff Salary")
    print("10. Search Staff")
    print("11. Add Attendance")
    print("12. View Attendance")
    print("13. Promote Staff")
    print("0. Exit")


def main():
    login()
    while True:
        menu()
        ch = input("Choose: ")

        if ch == "1": add_staff()
        elif ch == "2": update_staff()
        elif ch == "3": delete_staff()
        elif ch == "4": list_staff()
        elif ch == "5": add_dept()
        elif ch == "6": update_dept()
        elif ch == "7": delete_dept()
        elif ch == "8": list_dept()
        elif ch == "9": adjust_salary()
        elif ch == "10": search_staff()
        elif ch == "11": add_attendance()
        elif ch == "12": view_attendance()
        elif ch == "13": promote_staff()
        elif ch == "0": break
        else:
            print("Invalid choice!")
            pause()


if __name__ == "__main__":
    main()
