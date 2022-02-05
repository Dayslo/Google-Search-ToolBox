#!/usr/bin/env python3
###################################################
##              Dayslo - 02/2022               ##
## https://github.com/Dayslo/GoogleSearchToolBox ##
##                   Ver - 1.0                   ##
###################################################


import os
from googlesearch import search


print("""
   ___                _       ___                  _     
  / __|___  ___  __ _| |___  / __| ___ __ _ _ _ __| |_   
 | (_ / _ \/ _ \/ _` | / -_) \__ \/ -_) _` | '_/ _| ' \  
  \___\___/\___/\__, |_\___| |___/\___\__,_|_| \__|_||_| 
                |___/                                    
              _____         _ ___                        
             |_   _|__  ___| | _ ) _____ __              
               | |/ _ \/ _ \ | _ \/ _ \ \ /              
               |_|\___/\___/_|___/\___/_\_\              
                                                                     
""")

#Choice selection menu    
choice = input("""\
               [1] Find a Person or a Word
               [2] Search Website
               [3] Help / Search syntax
               [0] Exit
               >>> """)

#!!!--Clear the terminal--!!!
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#Return Menu
def MenuRetour():
    clearConsole()
    print("""
   ___                _       ___                  _     
  / __|___  ___  __ _| |___  / __| ___ __ _ _ _ __| |_   
 | (_ / _ \/ _ \/ _` | / -_) \__ \/ -_) _` | '_/ _| ' \  
  \___\___/\___/\__, |_\___| |___/\___\__,_|_| \__|_||_| 
                |___/                                    
              _____         _ ___                        
             |_   _|__  ___| | _ ) _____ __              
               | |/ _ \/ _ \ | _ \/ _ \ \ /              
               |_|\___/\___/_|___/\___/_\_\              
                                                                                                                    
""")
    choice = input("""\
               [1] Find a Person or a Word
               [2] Search Website
               [3] Help / More info
               [0] Exit
               >>> """)
    if choice == "1":
        Person()
    elif choice == "2":
        Website()
    elif choice == "3":
        Help()
    else:
        print("\nGood Bye")
        exit()


#Search for a person's first name or a word with ("")
def Person():
    try:
        p_query = input("\nEnter Enter a word or a person's name (Car or John Proz): ")
        queryperson = ('"' + p_query + '"')
        nomberperson = int(input("Enter the number of query: "))
        str_nomberperson = str(nomberperson)
        file_person = input("""\t
        [1] Default file
        [2] Create file
        >>> """)

        #Default file
        if file_person == "1":
            txt_Person_database_path = "database\Person_database.txt"
            Person_database = open(txt_Person_database_path, 'w')
            Person_database.write("Search " + queryperson + "\t" + "Number of websites " + str_nomberperson + "\n" * 2)
            #Search on Google with the values entered in the variables
            for url in search(queryperson, start=0 , stop=nomberperson, pause=2.0):
                Person_database.write("-" * 79 + "\n" * 2 + url + "\n" * 2)
            Person_database.close()
            print('\033[32m' + '\nSUCCESSFULLY, Save result ' + txt_Person_database_path + '\033[39m') 

        #Create file of the user 
        else:
            create_file_person = input('\nEnter the name of your file: ')
            extension_file_person = input('Enter your file extension: ')
            txt_create_file_person_database_path = "database" + "/" + create_file_person + "." + extension_file_person

            #Compare a file
            i = 0
            if os.path.exists(txt_create_file_person_database_path):
                    print('\033[31m' + 'File already exists' + '\033[39m')
                    i += 1
            else:
                #Create file
                create_file_person_database = open(txt_create_file_person_database_path, 'w')
                create_file_person_database.write("Valeur rechercher " + queryperson + "\tNombre de sortie " + str_nomberperson + "\n")
                #Search on Google with the values entered in the variables
                for url in search(queryperson, start=0 , stop=nomberperson, pause=2.0):
                    create_file_person_database.write(url + "\n")
                create_file_person_database.close()
                print('\033[32m' + '\nSUCCESSFULLY, Save result ' + txt_create_file_person_database_path + '\033[39m')
  
            while i == 1:
                    create_file_person = input('\nEnter the name of your file: ')
                    extension_file_person = input('Enter your file extension: ')
                    txt_create_file_person_database_path = "database" + "/" + create_file_person + "." + extension_file_person
                    if os.path.exists(txt_create_file_person_database_path):
                        print('\033[31m' + 'File already exists' + '\033[39m')
                    else:
                        i -=1
                        print(i)
                        #Create file
                        create_file_person_database = open(txt_create_file_person_database_path, 'w')
                        create_file_person_database.write("Valeur rechercher " + queryperson + "\tNombre de sortie " + str_nomberperson + "\n")
                        #Search on Google with the values entered in the variables
                        for url in search(queryperson, start=0 , stop=nomberperson, pause=2.0):
                            create_file_person_database.write(url + "\n")
                        create_file_person_database.close()
                        print('\033[32m' + '\nSUCCESSFULLY, Save result ' + txt_create_file_person_database_path + '\033[39m')
                        break            

    except:
        print('\033[31m' + '\nName and surname or number query is bad' + '\033[39m')

        tryagain = input("""\t
        [1] Try again
        [0] Exit
        >>> """)
        if tryagain == "1":
            Person()
        else:
            print("\nGood Bye")
            exit()

    returnmenu = input("""\t
        [1] Back to the menu
        [0] Exit
        >>> """)
    if returnmenu == "1":
        MenuRetour()
    else:
        print("\nGood Bye")
        exit()


#Find a site with (site:)
def Website():
    try:
        w_query = input("\nEnter the Website: ")
        querywebsite = ('site:' + w_query )
        nomberwebsite = int(input("Enter the number of query: "))
        str_nomberwebsite = str(nomberwebsite)
        file_website = input("""\t
        [1] Default file
        [2] Create file
        >>> """)

        #Default file
        if file_website == "1":
            txt_Website_database_path = "database\Website_database.txt"
            Website_database = open(txt_Website_database_path, 'w')
            Website_database.write("Valeur rechercher " + querywebsite + "\tNombre de sortie " + str_nomberwebsite + "\n")
            #Search on Google with the values entered in the variables
            for url in search(querywebsite, start=0 , stop=nomberwebsite, pause=2.0):
                Website_database.write(url + "\n")
            Website_database.close()
            print('\033[32m' + '\nSUCCESSFULLY, Save result ' + txt_Website_database_path + '\033[39m') 

        #Create file of the user 
        else:
            create_file_website = input('\nEnter the name of your file: ')
            extension_file_website = input('Enter your file extension: ')
            txt_create_file_website_database_path = "database" + "/" + create_file_website + "." + extension_file_website

            #Compare a file
            i = 0
            if os.path.exists(txt_create_file_website_database_path):
                    print('\033[31m' + 'File already exists' + '\033[39m')
                    i += 1
            else:
                #Create file
                create_file_website_database = open(txt_create_file_website_database_path, 'w')
                create_file_website_database.write("Valeur rechercher " + querywebsite + "\tNombre de sortie " + str_nomberwebsite + "\n")
                #Search on Google with the values entered in the variables
                for url in search(querywebsite, start=0 , stop=nomberwebsite, pause=2.0):
                    create_file_website_database.write(url + "\n")
                create_file_website_database.close()
                print('\033[32m' + '\nSUCCESSFULLY, Save result ' + txt_create_file_website_database_path + '\033[39m')
  
  
            while i == 1:
                    create_file_website = input('\nEnter the name of your file: ')
                    extension_file_website = input('Enter your file extension: ')
                    txt_create_file_website_database_path = "database" + "/" + create_file_website + "." + extension_file_website
                    if os.path.exists(txt_create_file_website_database_path):
                        print('\033[31m' + 'File already exists' + '\033[39m')
                    else:
                        i -=1
                        print(i)
                        #Create file
                        create_file_website_database = open(txt_create_file_website_database_path, 'w')
                        create_file_website_database.write("Valeur rechercher " + querywebsite + "\tNombre de sortie " + str_nomberwebsite + "\n")
                        #Search on Google with the values entered in the variables
                        for url in search(querywebsite, start=0 , stop=nomberwebsite, pause=2.0):
                            create_file_website_database.write(url + "\n")
                        create_file_website_database.close()
                        print('\033[32m' + '\nSUCCESSFULLY, Save result ' + txt_create_file_website_database_path + '\033[39m')
                        break            

    except:
        print('\033[31m' + '\nName and surname or number query is bad' + '\033[39m')

        tryagain = input("""\t
        [1] Try again
        [0] Exit
        >>> """)
        if tryagain == "1":
            Website()
        else:
            print("\nGood Bye")
            exit()

    returnmenu = input("""\t
        [1] Back to the menu
        [0] Exit
        >>> """)
    if returnmenu == "1":
        MenuRetour()
    else:
        print("\nGood Bye")
        exit()


def Help():
    help1 = ('\033[1m' + "search syntax (John Proz) or (Car)" + '\033[0m')
    help2 = ('\033[1m' + "search syntax (website.com, .fr .be ... or .* for everything)" + '\033[0m')

    info = """
    (1) Find a Person with the operator Google (""), """ + help1 + """
    (2) Search website with the operator Google (site:), """ + help2 + """
    """
    print(info)

    returnmenu = input("""\
    [1] Back to the menu
    [0] Exit
    >>> """)
    if returnmenu == "1":
        MenuRetour()
    else:
        print("\nGood Bye")
        exit()

    
    

#Initialization of menu variables
if choice == "1":
    Person()
elif choice == "2":
    Website()
elif choice == "3":
    Help()
else:
    print("\nGood Bye")
    exit()
