import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name{filename}:created successfully!")
    except FileExistsError: #if the file already exist
        print(f"File Name{filename} already exists!")
    except Exception as e:
        print("An error occured")

def view_all_files():
    files=os.listdir()
    if not files:
        print("No file found!")
    else:
        print("File is in Directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print('An error occured!')


def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f"content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exist!") 
    except Exception as e:
        print("An error occured!")


def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("Enter data to add=")
            f.write(content+"\n")
            print(f"content added to {filename} Succesfully")
    except FileNotFoundError:
        print(f"{filename} does not exist!") 
    except Exception as e:
        print("An error occured!")


def main():
    while True:
        print("WELCOME TO FILE MANAGEMENT APP")
        print("1:Create file")
        print("2:View all files")
        print("3:Delete file")
        print("4:Read file")
        print("5:Edit file")
        print("6:Exit")

        choice=input("Enter your Choice (1-6):")

        if choice =='1':
            filename=input("Enter the file-name to create = ")
            create_file(filename)

        elif choice =='2':
            view_all_files()

        elif choice =='3':
            filename=input("enter the filename you want to delete = ")
            delete_file(filename)

        elif choice =='4':
            filename=input("Enter the filename you want to read = ")
            read_file(filename)

        elif choice =='5':
            filename=input("Enter the filename you want to edit = ")
            edit_file(filename)
        
        elif choice =='6':
            print("closing the app.....")
            break

        else:
            print("In-valid Number")

if __name__ == "__main__":
    main()



