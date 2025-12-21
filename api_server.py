from fastapi import FastAPI
import os

app = FastAPI(title="StaffManager Pro with API and File Support")

USER_FILE = "users.txt"
STAFF_FILE = "staff.txt"
DEPT_FILE = "departments.txt"
ATT_FILE = "attendance.txt"

def read_file(path):
    if not os.path.exists(path):
        open(path, "w").close()
        return []
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def write_file(path, rows):
    with open(path, "w") as f:
        f.write("\n".join(rows))



def ensure_admin():
    if not read_file(USER_FILE):
        write_file(USER_FILE, ["admin|1234"])

ensure_admin()



@app.post("/login")
def login(username: str, password: str):
    try:
        users = read_file(USER_FILE)
        for u in users:
            u_name, u_pass = u.split("|")
            if username == u_name and password == u_pass:
                return "LOGIN SUCCESS"
        return "INVALID LOGIN"
    except:
        return "ERROR: Could not process login"



def dept_exists(dept_id):
    return any(d.split("|")[0] == dept_id for d in read_file(DEPT_FILE))


@app.post("/department/add")
def department_add(dept_id: str, name: str):
    try:
        depts = read_file(DEPT_FILE)
        if dept_exists(dept_id):
            return "DEPARTMENT ALREADY EXISTS"
        depts.append(f"{dept_id}|{name}")
        write_file(DEPT_FILE, depts)
        return "DEPARTMENT ADDED"
    except:
        return "ERROR: Could not add department"


@app.post("/department/update")
def department_update(dept_id: str, name: str):
    try:
        depts = read_file(DEPT_FILE)
        for i in range(len(depts)):
            if depts[i].split("|")[0] == dept_id:
                depts[i] = f"{dept_id}|{name}"
                write_file(DEPT_FILE, depts)
                return "DEPARTMENT UPDATED"
        return "DEPARTMENT NOT FOUND"
    except:
        return "ERROR: Could not update department"


@app.post("/department/delete")
def department_delete(dept_id: str):
    try:
        depts = read_file(DEPT_FILE)
        new_list = [d for d in depts if d.split("|")[0] != dept_id]
        if len(new_list) == len(depts):
            return "DEPARTMENT NOT FOUND"
        write_file(DEPT_FILE, new_list)
        return "DEPARTMENT DELETED"
    except:
        return "ERROR: Could not delete department"


@app.get("/department/list")
def department_list():
    try:
        rows = read_file(DEPT_FILE)
        if not rows:
            return "NO DEPARTMENTS FOUND"
        return "\n".join(rows)
    except:
        return "ERROR: Could not load departments"



@app.post("/staff/add")
def staff_add(staff_id: str, name: str, dept_id: str, position: str, salary: str):
    try:
        if not dept_exists(dept_id):
            return "ERROR: ADD DEPARTMENT FIRST"

        staffs = read_file(STAFF_FILE)
        if any(s.split("|")[0] == staff_id for s in staffs):
            return "STAFF ALREADY EXISTS"

        staffs.append(f"{staff_id}|{name}|{dept_id}|{position}|{salary}")
        write_file(STAFF_FILE, staffs)
        return "STAFF ADDED"
    except:
        return "ERROR: Could not add staff"


@app.post("/staff/update")
def staff_update(staff_id: str, name: str, dept_id: str, position: str, salary: str):
    try:
        staffs = read_file(STAFF_FILE)
        for i in range(len(staffs)):
            if staffs[i].split("|")[0] == staff_id:
                staffs[i] = f"{staff_id}|{name}|{dept_id}|{position}|{salary}"
                write_file(STAFF_FILE, staffs)
                return "STAFF UPDATED"
        return "STAFF NOT FOUND"
    except:
        return "ERROR: Could not update staff"


@app.post("/staff/delete")
def staff_delete(staff_id: str):
    try:
        staffs = read_file(STAFF_FILE)
        new_list = [s for s in staffs if s.split("|")[0] != staff_id]
        if len(new_list) == len(staffs):
            return "STAFF NOT FOUND"
        write_file(STAFF_FILE, new_list)
        return "STAFF DELETED"
    except:
        return "ERROR: Could not delete staff"


@app.get("/staff/list")
def staff_list():
    try:
        rows = read_file(STAFF_FILE)
        if not rows:
            return "NO STAFF FOUND"
        return "\n".join(rows)
    except:
        return "ERROR: Could not load staff list"


@app.get("/staff/search")
def staff_search(name: str):
    try:
        rows = read_file(STAFF_FILE)
        result = [r for r in rows if name.lower() in r.lower()]
        if not result:
            return "NO MATCH FOUND"
        return "\n".join(result)
    except:
        return "ERROR: Could not search staff"


@app.post("/staff/adjust_salary")
def adjust_salary(staff_id: str, change: float):
    try:
        staffs = read_file(STAFF_FILE)
        for i in range(len(staffs)):
            s = staffs[i].split("|")
            if s[0] == staff_id:
                new_salary = float(s[4]) + change
                staffs[i] = f"{s[0]}|{s[1]}|{s[2]}|{s[3]}|{new_salary}"
                write_file(STAFF_FILE, staffs)
                return "SALARY UPDATED"
        return "STAFF NOT FOUND"
    except:
        return "ERROR: Could not adjust salary"


@app.post("/staff/promote")
def promote(staff_id: str, new_position: str):
    try:
        staffs = read_file(STAFF_FILE)
        for i in range(len(staffs)):
            s = staffs[i].split("|")
            if s[0] == staff_id:
                staffs[i] = f"{s[0]}|{s[1]}|{s[2]}|{new_position}|{s[4]}"
                write_file(STAFF_FILE, staffs)
                return "STAFF PROMOTED"
        return "STAFF NOT FOUND"
    except:
        return "ERROR: Could not promote staff"



@app.post("/attendance/add")
def attendance_add(staff_id: str, date: str, status: str):
    try:
        with open(ATT_FILE, "a") as f:
            f.write(f"{staff_id}|{date}|{status}\n")
        return "ATTENDANCE ADDED"
    except:
        return "ERROR: Could not add attendance"


@app.get("/attendance/summary")
def attendance_summary(staff_id: str):
    try:
        if not os.path.exists(ATT_FILE):
            return "NO ATTENDANCE RECORDS FOUND"

        rows = read_file(ATT_FILE)
        result = [r for r in rows if r.split("|")[0] == staff_id]
        if not result:
            return "NO RECORDS FOUND"
        return "\n".join(result)
    except:
        return "ERROR: Could not load attendance"
