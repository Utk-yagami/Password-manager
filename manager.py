import ast
m_password = input('Enter master password: ')

if(m_password=="sachin"):
    with open("myfile.txt","r") as f:
        password_manager=f.read()
        print(password_manager)
else:
    print("Wrong m_password")