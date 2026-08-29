requests = []
while True:
    print("1. Add a request")
    print("2. view all requests")
    print("3. Search by name")
    print("4. Add new note")
    print("5. Total requests")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        name = input("Enter your name : ")
        status = input("Enter status : ")
        goal = input("Enter your goal : ")
        note ="Currently not added"

        request = {
            "Name": name,
            "Status": status,
            "Goal":goal,
            "Note":note
        }
        requests.append(request)
        print("Request added successfully")

    elif choice== "2":
        if len(requests) == 0:
            print("No requests found.")
        else:
            for index, request in enumerate(requests, start=1):
                print("Request", index ,":")
                print("Name:", request["Name"])
                print("Status:", request["Status"])
                print("Goal:", request["Goal"])
                print("Note :",request["Note"])

    elif choice == "3":
        name_search = input("Enter the name : ")
        for request in requests :
            if name_search == request["Name"] :
                print("The request is :")
                print("Name:", request["Name"])
                print("Status:", request["Status"])
                print("Goal:", request["Goal"])
            else :
                print("The request not founded")

    elif choice =="4" :
        name_search =input("Enter your name :")
        for request in requests :
            if name_search==request["Name"] :
                print("The request is :")
                request["Note"]=input("Add your note :")
                print("Note added successfully")
                break
            else :
                print("The request not founded")

    elif choice =="5":
            Total_requests=len(requests)
            print("Total requests" ,":",Total_requests)

    elif choice =="6":
        print("Thank you! Your requests have been saved.")
        break