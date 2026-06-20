import csv
import os

FILENAME="contacts.csv"
if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["Name","Phone","Email"])

def addContact():
    name=input("Name: ").strip()
    phone=input("Phone: ").strip()
    email=input("Email: ").strip()

    #duplicates checking
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("That name already exists !!")
                return
    with open(FILENAME,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow([name,phone,email])
        print("Contact Added")

def view_contacts():
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        rows=list(reader)

        if len(rows)<1:
            print("No Contacts Found")
            return
        print("Your Contacts : \n")
        for row in rows[1:]:
            if len(row)==3:
                print(f"{row[0]} | {row[1]} | {row[2]}")
        print()
            
def search_contact():
    term=input("Enter a name to search - ").strip().lower()
    found = False
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row:
                if len(term)==3:
                    print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                    found=True
    if not found:
        print("No matching contact found")
    
def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View All Contact")
        print("3. Search Contact")
        print("4. Exit")

        choice = int(input("Choose option (1-4) - "))

        if choice==1:
            addContact()
        elif choice==2:
            view_contacts()
        elif choice==3:
            search_contact()
        elif choice==4:
            print("Thanks for using our software")
            break
        else:
            print("Invalid chice of number")

if __name__=="__main__":
    main()

