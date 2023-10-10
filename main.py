import csv 

print("Welcome to our pet store! Enter 1 for cats and 2 for dogs.")
try:
    option = int(input("Please enter a number:"))
        
except:
    print("Please only input values of 1 or 2")
 
if option == 1:
    try:
        #print("hi, I work!")
        with open ('./data/cats.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(f"Here is our cat:\nName: {row['name']},\nAge: {row[' age']},\nBreed: {row[' breed']}")
    except FileNotFoundError:
            print('File not found!')
    except Exception as e:
            print('An error occured: {e}')     

elif option == 2:
    try:
        with open ('./data/dogs.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(f"Here is our dog: \nName: {row['name']}, \nAge: {row[' age'].strip()}, \nBreed: {row[' breed'].strip()}")
    except FileNotFoundError:
             print('File not found!')
    except Exception as e:
             print('An error occured: {e}')  

     
        