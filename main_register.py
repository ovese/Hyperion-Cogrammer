from student_register import StudentRegister

sr = StudentRegister('admin')


def main():
    [all_users, all_roles] = sr.read_user_names_roles()
    print("Authenticated Users: ")
    sr.display_utility(all_users)
    print("\n")
    print("Authenticated Roles: ")
    sr.display_utility(all_roles)
    print("\n")

    # validate user
    # [current_user, current_role] = sr.validate_user()
    # print(f"Current user is: {current_user} \n"
    #       f"with role as: {current_role}")

    # get number of students to reguister
    number_of_students_to_reg = sr.get_num_students()

    # start refistration
    sr.execute_registration(number_of_students_to_reg)


if __name__ == '__main__':
    main()
