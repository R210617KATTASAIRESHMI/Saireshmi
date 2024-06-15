from PIL import Image
import csv
image = Image.open("/home/rguktrkvalley/computational lab/week8/1701322810442.png")

rgb_values=list(image.getdata())

with open('rgb_values.csv',mode='w')as file:
   writer=csv.writer(file)
   
   writer.writerow(['red','green','blue'])
   
   for rgb in rgb_values:
       writer.writerow(rgb)
       
print("rgb values have been writen to rgb_values.csv file")
