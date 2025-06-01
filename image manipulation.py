from PIL import  Image
import os

def manipulate_image():
    
  image = input("Input the name of the image with the extension you want to manipulate (e.g cat.png):")

  actual_image = Image.open(f"{image}").convert("RGBA")
  image_data = list(actual_image.getdata())
  
  for i, pixel in enumerate(image_data):
   if pixel[:4] == (0, 0, 0, 0):
     image_data[i] = (255, 255, 255, 255)

   R = pixel[0]
   G = pixel[1]
   B = pixel[2]
   A = pixel[3]

   image_data[i] = (255 - R, 255 - G, 255 - B, A)
  new_name = os.path.splitext(image)[0] + "_manipulated.png"
  actual_image.putdata(image_data)
  actual_image.save(f"{new_name}")
  print(f"{new_name} created successfully.")

manipulate_image()