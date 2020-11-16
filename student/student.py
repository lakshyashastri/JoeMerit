import os
import MySQLdb


from student.helpers_student import *
from student.options_student import *
from student.sql_functions_student import *



db = MySQLdb.connect(host = "localhost", user = "root", passwd = os.environ['sqlpwd'])
cursor = db.cursor()




#table name template = "student_id--student_pw"



qwe("SHOW DATABASES")
if ('students', ) not in cursor.fetchall():
    qwe("CREATE DATABASE students")
    db.commit()




#login/sign_up process
while True:

    qwe("USE students")
    display_options(first_prompt)

    while True:

        #login/sign-up?
        first_choice = get_choice(first_prompt)

        #sign-up
        if first_choice == 1:


            new_id = input("Enter a unique username: ")
            qwe("SHOW TABLES")
            for table_name in cursor.fetchall():
                if table_name.split(" | ")[0] == new_id:
                    print("This username has already been taken. Please choose a different username.")
                    break


            new_pw = input("Enter password: ")
            new_pw_confirm = input("Confirm password: ")

            if new_pw != new_pw_confirm:
                print("The entered passwords do not match. Please try again.")
                break
            

            # still have to add table columns. Might add datetime to store when their acc/ID was created.
            qwe(f"CREATE TABLE {get_table_name(new_id,new_pw)}")
            print("New ID created. Returning to the previous page.")
            break
        

        #login
        elif first_choice == 2:


            login_id = input("Enter your student ID: ")
            login_pw = input("Enter your password: ")


            qwe("SHOW TABLES")
            for table_name in cursor.fetchall():

                if get_table_name(login_id,login_pw) == table_name:
                    print("Logged in successfully.")
                    break
                
                else:
                    print("The entered credentials may be wrong. Please try again.")
                    break
        break
    break





#WIP
while True:

    while True:

        #displaying available tests and getting a test choice for them to attempt

        display_options(get_test_name_dict())

        get_choice(get_test_name_dict())

        

        
        