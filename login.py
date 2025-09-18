import streamlit as st
from db2 import get_connection
from app import show_app
from daftar import show_register

st.set_page_config(page_title="Login Page", page_icon="🔐")

# Init session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

def login_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        if conn is None:
            st.error("Gagal koneksi ke database!")
        elif username == "" or password == "":
            st.error("Username / Password tidak boleh kosong.")
        else:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if result:
                st.session_state.logged_in = True
                st.session_state.page = "app"
                st.experimental_rerun()
            else:
                st.error("Username / Password salah.")

    if st.button("Daftar jika belum ada akun"):
        st.session_state.page = "register"
        st.experimental_rerun()

# Router
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "app":
    show_app()
elif st.session_state.page == "register":
    show_register()
