from Login import Login
import sqlite3
def main():
    login = Login()

    while True:
        print("请选择：")
        print("1. 注册")
        print("2. 登录")
        print("3. 退出")

        choice = input("请输入选项：")

        if choice == "1":
            try:
                username = input("请输入用户名：")
                password = input("请输入密码：")
                login.add_user(username, password)
            except  sqlite3.IntegrityError as e:
                print(f"用户名已存在，请登录或更换用户名")
        elif choice == "2":
            username = input("请输入用户名：")
            password = input("请输入密码：")
            login.log_in(username, password)
        elif choice == "3":
            print("退出程序")
            break
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()