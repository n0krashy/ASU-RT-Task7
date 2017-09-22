def opencsv():
    "This function create new CSV file"
    import csv
    with open('users.csv', 'w') as csvfile:
        fieldnames = ['Name', 'Email', 'Mobile', 'University', 'Major']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def printcsv():
    "This function writes into CSV file"
    import csv
    with open('users.csv', 'a') as csvfile:
        fieldnames = ['Name', 'Email', 'Mobile', 'University', 'Major']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Email': email, 'Mobile': mobile, 'University': univ, 'Major': major})


def stop(s):
    "This function checks if user entered stop & end program if so"
    if s == "STOP" or s == "stop":
        import sys
        sys.exit()


opencsv()
while True:

    while True:
        name = raw_input("\nName: ")
        stop(name)
        if name:
            break
        else:
            print ("\n\tThis is required info.")

    while True:
        email = raw_input("\nEmail: ")
        stop(email)
        if '@' in email and '.com' in email:
            break
        else:
            print ("\n\tPlease enter valid email address.")

    while True:
        mobile = raw_input("\nMobile: ")
        stop(mobile)
        if mobile.isdigit():
            break
        else:
            print ("\n\tPlease enter valid mobile number.")

    while True:
        univ = raw_input("\nUniversity: ")
        stop(univ)
        if univ:
            break
        else:
            print ("\n\tThis is required info.")

    while True:
        major = raw_input("\nMajor: ")
        stop(major)
        if major:
            break
        else:
            print ("\n\tThis is required info.")

    printcsv()
