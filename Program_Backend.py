import os
from  PIL import Image as im
import pandas as pd

location = os.path.dirname(__file__)
os.chdir(location)
photo_folder=location+'\\Pics'

photo_list = os.listdir(photo_folder)
Main=im.open('Pics\\'+ photo_list[-1])

def img_ref_assigner(refno):
    for photo in photo_list:
        if str(refno) in photo:
            return (photo[:1])
            break

def photo_selector(img_ref):
    if img_ref == None: #Thus photo_selector should not return anything
        return None
    else:
        for photo in photo_list:
            if photo[:1] == img_ref:
                return(photo)
            else:
                continue

class Component:
    def __init__(self,name,description,ref_no):
        self.name =  name
        self.ds =  description
        self.refno = ref_no
        self.img_ref = img_ref_assigner(ref_no)

    def image(self):
        photo_name = photo_selector(self.img_ref)
        if photo_name == None:
            print('NO ASSOCIATED PICTURE, NOT TESTED') #And no photo.
        else:
            img_file = im.open('Pics\\'+ photo_name)
            img_file.show()


#Initialization Sequence
data = pd.read_csv("Component Data.csv")

Name_list_1 = data.iloc[:,0]
Name_list = Name_list_1.values.tolist()

untested_bool = data['Ref.']=='-'
Untested_list = data[untested_bool].iloc[:,0].reset_index()

tested_bool = data['Ref.']!='-'
Tested_list = data[tested_bool].iloc[:,0].reset_index()

Component_list=[]
index = data.index

Component_count = 0
for i in index: #Create list of components
    Component_list.append(Component(data.iloc[i,0],data.iloc[i,1],data.iloc[i,2]))
    Component_count += 1
print(Component_count, 'Components created')

