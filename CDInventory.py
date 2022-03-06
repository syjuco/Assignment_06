#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# SSyjuco, 2022-Mar-05, Modified File to complete Assignment06 Requirements. You can follow the # comments from top to bottom to track my changes. 
#------------------------------------------#

# -- DATA -- # I did not have to make any changes to this DATA section
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- # I added 4 new functions: add_cd():, delete_cdfr_memory():, write_file(file_name, table):, input_cd():
class DataProcessor:
    """Processing the data to and from memory"""
    # TO Done added functions for processing here. # Added two out of four functions in this class, add_cd(): and delete_cdfr_memory():
    @staticmethod
    def add_cd():
        """ Function to add CD details to memory
        
        Args: 
            None.
        
        Returns:
            newlst = [] # need to define a list receive the results of the input_cd() 
            newlst = IO.input_cd() # this captures the user CD input from another function (will discuss in the IO class below) and converts to a list
            dicRow = {'ID': newlst[0], 'Title': newlst[1], 'Artist': newlst[2]} # the dictionary keys can now receive the inputs from the newlst indices
            lstTbl.append(dicRow) # dicRow can now be appended to lstTbl as usual
            IO.show_invenotry(lstTbl) # this calls the IO function show_inventory(lstTbl) to confirm to the user what was added to the table 
        
        
        """
        newlst = []
        newlst = IO.input_cd()
        dicRow = {'ID': newlst[0], 'Title': newlst[1], 'Artist': newlst[2]}
        lstTbl.append(dicRow)
        return IO.show_inventory(lstTbl)
    
    
    @staticmethod
    def delete_cdfr_memory():
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        
        
class FileProcessor: # I added the third out of four functions in this class, write_file(file_name, table):
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table): 
        """Function to save the CDs currently in memory to the text file CDInventory.txt
        
        Args:
            None.
        
        Returns: 
            None. 
        
        
        """
        # TO Done Added code here 
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #

class IO: #I added the fourth out of four functions here, input_cd():  
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod    
    def input_cd():
        """Function to ask the user for CD details to add to memory: CD's ID, CD title, Artist
        
        Args:
            None. 
        
        Returns: 
            strID = input('Enter ID: ').strip() # asks the user for their desired ID to assign to the CD
            strTitle = input('What is the CD\'s title? ').strip() # asks the user to input the CDs title
            stArtist = input('What is the Artist\'s name? ').strip() #asks the user to input the Artist of the CD
            return [strID, strTitle, stArtist] #returns the result of the three inputs as a list. this is important for the add_cd(): function to get a list result to process. 
        
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return [strID, strTitle, stArtist]
    

# TO Done added I/O functions as needed, added the input_cd(): above

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TO Done moved IO code into function
        # 3.3.2 Add item to the table
        # TO Done moved processing code into function
        DataProcessor.add_cd() #This function combines steps 3.3.1 and 3.3.2
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # TO Done moved processing code into function
        DataProcessor.delete_cdfr_memory() #This is the new function that was defined 
        IO.show_inventory(lstTbl) # this displays the updated CDs in memory
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TO Done move processing code into function
            FileProcessor.write_file(strFileName, lstTbl) #Added this new function to process the saving of memory to strFileName
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




