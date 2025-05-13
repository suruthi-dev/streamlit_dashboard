import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

df = pd.read_csv('userdata.csv')
users = df['username'].values
passwords = df['password'].values


hashed_passwords = stauth.Hasher(passwords).generate()


authenticator = stauth.Authenticate(names=users,
                                   passwords=hashed_passwords,
                                   usernames=users,
                                   cookie_name="auth_cookie",key="key1",
                                   cookie_expiry_days=30)


# --- LOGIN ---

name, auth_status, username = authenticator.login("Login", "main")


# --- LOGIC ---
if auth_status is False:
    st.error("Invalid username or password")

elif auth_status is None:
    st.warning("Please enter your login credentials")

elif auth_status:
    # Logged in
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name}")
    
    st.title("Dashboard")
    option = st.sidebar.radio("Navigate", ["Page 1", "Page 2"])
    if option == "Page 1":
        st.write("You're on Page 1")
    else:
        st.write("You're on Page 2")
        


# import streamlit as st
# import pandas as pd
# import streamlit_authenticator as stauth


# df = pd.read_csv("userdata.csv")

# existing_username = df['username'].values[0]
# existing_password = df['password'].values[0]

# # hashed_existing_pw = stauth.Hasher(existing_password).generate()

# with st.form("user_form"):
#     login_username = st.text_input("Username")
#     login_password = st.text_input("Password", type="password")
#     submit = st.form_submit_button("Login")

# if submit:
#     # Check if the entered username matches the stored username
#     if login_username == existing_username:
#         # Hash the entered password and compare with stored hash
#         hashed_login_pw = stauth.Hasher([login_password]).generate()[0]
        
#         if hashed_login_pw == existing_password:
#             # Authentication success, redirect to main page
#             st.session_state.authenticated = True
#             # st.experimental_rerun()  # This will trigger a rerun of the app, where we can check for login state

#         else:
#             st.error("Incorrect password.")
#     else:
#         st.error("Username not found.")

# # -----------------------------
# # STEP 4: Main Page Redirect on Successful Authentication
# # -----------------------------
# if "authenticated" in st.session_state and st.session_state.authenticated:
#     # User is authenticated, redirect to main dashboard
#     st.title("Main Dashboard")
#     st.sidebar.radio("Select Page", ["Page 1", "Page 2"])
#     st.write("Welcome to the main page!")
