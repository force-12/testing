import psycopg2

def get_connection():
    """
    Fungsi koneksi ke Supabase PostgreSQL
    Mengembalikan objek connection atau None kalau gagal
    """
    try:
        conn = psycopg2.connect(
            "postgresql://postgres.gyohfzvugbusjcbsmffu:%40Mrcyber12345@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres"
)
        print("[DB] Koneksi berhasil!")  # terminal
        return conn
    except Exception as e:
        print(f"[DB] Gagal koneksi: {e}")  # terminal
        return None

# -------------------------
# CRUD Siswa
# -------------------------
def create_siswa(NIM, Nama, Angkatan, Email):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO siswa ("NIM","Nama","Angkatan","Email") VALUES (%s, %s, %s, %s)',
                (NIM, Nama, Angkatan, Email)
            )
        conn.commit()
        conn.close()

def read_siswa():
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT id,"NIM","Nama","Angkatan","Email" FROM siswa ORDER BY id ASC')
            result = cursor.fetchall()
        conn.close()
        return result
    return []

def update_siswa(NIM, Nama, Angkatan, Email):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'UPDATE siswa SET "Nama"=%s, "Angkatan"=%s, "Email"=%s WHERE "NIM"=%s',
                (Nama, Angkatan, Email, NIM)
            )
        conn.commit()
        conn.close()

def delete_siswa(NIM):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM siswa WHERE "NIM"=%s', (NIM,))
        conn.commit()
        conn.close()

def search_siswa(NIM):
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT id,"NIM","Nama","Angkatan","Email" FROM siswa WHERE "NIM"=%s', (NIM,))
            result = cursor.fetchall()
        conn.close()
        return result
    return []