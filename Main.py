import Program_Backend

print("Welcome to MS2 Trainer!")
print("Options: \n Component List \n Tested List \n Untested List \n Main Image \n Name of Any Component \n Quit")


while True:
    command = input("Please input an option")
    if command == "Component List":
        print(Program_Backend.Name_list_1)
    elif command == 'Tested List':
        print(Program_Backend.Tested_list)
    elif command == 'Untested List':
        print(Program_Backend.Untested_list)
    elif command == "Main Image":
        Program_Backend.Main.show()
        continue
    elif command in Program_Backend.Name_list:
        c_idx = Program_Backend.Name_list.index(command)
        print('Description:',Program_Backend.Component_list[c_idx].ds)
        print('Reference No.:',Program_Backend.Component_list[c_idx].refno)
        Program_Backend.Component_list[c_idx].image()
        continue
    elif command == 'Quit':
        break
    
