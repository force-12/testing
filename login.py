import streamlit as st
from db2 import get_connection

st.set_page_config(page_title="Login Page", page_icon="🔐")
st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.button("Login"):
    conn = get_connection()
    if conn is None:
        st.error("Gagal koneksi ke database!")
    elif username == "" or password == "":
        st.error("Username / Password tidak boleh kosong.")
    else:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            if result:
                st.session_state['logged_in'] = True
                st.success("Login berhasil!")
                st.switch_page("pages/app.py")
            else:
                st.error("Username / Password salah.")
        except Exception as e:
            st.error(f"Gagal login: {e}")
        finally:
            cursor.close()
            conn.close()

if st.button("Daftar jika belum ada akun"):
    st.switch_page("pages/daftar.py")
