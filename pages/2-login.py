import streamlit as st
import pandas as pd
import sqlite3 
import hashlib

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management

conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username,password))
	data = c.fetchall()
	return data

def create_sessiontable():
	c.execute('CREATE TABLE IF NOT EXISTS sessiontable(username TEXT,password TEXT)')

def start_session(username, password):
	c.execute('DELETE FROM sessiontable')
	conn.commit()
	c.execute('INSERT INTO sessiontable(username,password) VALUES (?,?)', (username,password))
	conn.commit()

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def view_session():
	c.execute('SELECT * FROM sessiontable')
	data = c.fetchall()
	return data



def main():
	st.title("Sign in")
	menu = ["Login","SignUp"]
	choice = st.selectbox("Menu",menu)

	if choice == "Login":
		st.subheader("Login Section")

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		if st.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				create_sessiontable()
				start_session(username, hashed_pswd)
				#st.write(view_session())

				st.success("Logged In as {}".format(username))
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

if __name__ == '__main__':
	main()