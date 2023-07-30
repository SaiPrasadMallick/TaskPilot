# user.py

import os
import datetime

def user_information(username, password):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    user_data = {
        "username": username,
        "password": password,
        "name": name,
        "address": address,
        "age": age
    }
    save_user_data(user_data)

def save_user_data(user_data):
    username = user_data["username"]
    file_name = username + "_task.txt"
    with open(file_name, "w") as f:
        f.write(user_data["password"] + "\n")
        f.write("Name: " + user_data["name"] + "\n")
        f.write("Address: " + user_data["address"] + "\n")
        f.write("Age: " + user_data["age"] + "\n")

def get_user_data(username):
    file_name = username + "_task.txt"
    user_data = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            user_data["password"] = lines[0].strip()
            user_data["name"] = lines[1].replace("Name: ", "").strip()
            user_data["address"] = lines[2].replace("Address: ", "").strip()
            user_data["age"] = lines[3].replace("Age: ", "").strip()
    return user_data

def check_login(username, password):
    user_data = get_user_data(username)
    return user_data["password"] == password
