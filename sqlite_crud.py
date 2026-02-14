import sqlite3
from sqlite3 import Error

# ---------- FUNKCJE POMOCNICZE ----------
def create_connection(db_file):
    """ Tworzy połączenie z bazą SQLite i zwraca obiekt połączenia """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Połączenie z bazą nawiązane.")
    except Error as e:
        print(f"Błąd połączenia: {e}")
    return conn

def create_tables(conn):
    """ Tworzy tabele projects i tasks, jeśli nie istnieją """
    try:
        cur = conn.cursor()
        # Tabela projects
        cur.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT NOT NULL,
                start_date TEXT,
                end_date TEXT
            )
        ''')
        # Tabela tasks (z kluczem obcym do projects)
        cur.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER,
                nazwa TEXT NOT NULL,
                opis TEXT,
                status TEXT,
                start_date TEXT,
                end_date TEXT,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        ''')
        conn.commit()
        print("Tabele utworzone lub już istniały.")
    except Error as e:
        print(f"Błąd tworzenia tabel: {e}")

# ---------- CREATE (DODAWANIE) ----------
def add_project(conn, nazwa, start_date, end_date):
    """ Dodaje nowy projekt do tabeli projects """
    sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (nazwa, start_date, end_date))
    conn.commit()
    return cur.lastrowid   # zwraca ID nowego projektu

def add_task(conn, project_id, nazwa, opis, status, start_date, end_date):
    """ Dodaje nowe zadanie do tabeli tasks """
    sql = '''INSERT INTO tasks(project_id, nazwa, opis, status, start_date, end_date)
             VALUES(?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (project_id, nazwa, opis, status, start_date, end_date))
    conn.commit()
    return cur.lastrowid

# ---------- READ (POBIERANIE) ----------
def select_all_projects(conn):
    """ Zwraca listę wszystkich projektów """
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")
    rows = cur.fetchall()
    return rows

def select_all_tasks(conn):
    """ Zwraca listę wszystkich zadań """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    return rows

def select_tasks_by_project(conn, project_id):
    """ Zwraca wszystkie zadania dla danego projektu """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id,))
    rows = cur.fetchall()
    return rows

# ---------- UPDATE (AKTUALIZACJA) ----------
def update_task_status(conn, task_id, new_status):
    """ Aktualizuje status zadania o podanym ID """
    sql = '''UPDATE tasks SET status = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (new_status, task_id))
    conn.commit()
    print(f"Zaktualizowano {cur.rowcount} wiersz(y).")

# ---------- DELETE (USUWANIE) ----------
def delete_task(conn, task_id):
    """ Usuwa zadanie o podanym ID """
    sql = "DELETE FROM tasks WHERE id = ?"
    cur = conn.cursor()
    cur.execute(sql, (task_id,))
    conn.commit()
    print(f"Usunięto {cur.rowcount} wiersz(y).")

def delete_all_tasks(conn):
    """ Usuwa wszystkie zadania (OSTROŻNIE!) """
    sql = "DELETE FROM tasks"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(f"Usunięto wszystkie zadania ({cur.rowcount} wierszy).")

# ---------- GŁÓWNY PROGRAM (DEMONSTRACJA) ----------
if __name__ == "__main__":
    # 1. Połączenie z bazą (plik database.db)
    with create_connection("database.db") as conn:
        if conn is None:
            exit(1)

        # 2. Utworzenie tabel
        create_tables(conn)

        # 3. Dodanie przykładowego projektu
        print("\n--- Dodawanie projektu ---")
        pr_id = add_project(conn, "Nauka SQL", "2025-03-01", "2025-03-10")
        print(f"Dodano projekt z ID = {pr_id}")

        # 4. Dodanie kilku zadań dla tego projektu
        print("\n--- Dodawanie zadań ---")
        task1_id = add_task(conn, pr_id, "Przeczytaj rozdział 1", "Wprowadzenie do SQL", "started", "2025-03-01", "2025-03-02")
        task2_id = add_task(conn, pr_id, "Wykonaj ćwiczenia", "Ćwiczenia z SELECT", "pending", "2025-03-03", "2025-03-05")
        print(f"Dodano zadania: ID {task1_id}, {task2_id}")

        # 5. Pobieranie i wyświetlanie wszystkich projektów
        print("\n--- Lista projektów ---")
        projekty = select_all_projects(conn)
        for p in projekty:
            print(p)

        # 6. Pobieranie zadań dla projektu
        print(f"\n--- Zadania dla projektu ID {pr_id} ---")
        zadania = select_tasks_by_project(conn, pr_id)
        for z in zadania:
            print(z)

        # 7. Aktualizacja statusu pierwszego zadania
        print("\n--- Aktualizacja statusu zadania ---")
        update_task_status(conn, task1_id, "done")

        # 8. Sprawdzenie zmiany
        print("\n--- Zadania po aktualizacji ---")
        zadania2 = select_tasks_by_project(conn, pr_id)
        for z in zadania2:
            print(z)

        # 9. Usunięcie drugiego zadania
        print("\n--- Usuwanie zadania ---")
        delete_task(conn, task2_id)

        # 10. Sprawdzenie po usunięciu
        print("\n--- Zadania po usunięciu ---")
        zadania3 = select_tasks_by_project(conn, pr_id)
        if zadania3:
            for z in zadania3:
                print(z)
        else:
            print("Brak zadań dla tego projektu.")

        # 11. Opcjonalnie: usunięcie wszystkich zadań (odkomentuj, jeśli chcesz wyczyścić)
        # delete_all_tasks(conn)

    print("\nKoniec programu. Połączenie zamknięte.")
    