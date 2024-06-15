from PIL import image
image_path=''
image=image.open('/home/rguktrkvalley/computational lab/week8/1701322810442.png')
x,y=100,100
rgb=image.getpixel((x,y))
print(f'RGB values at position ({x},{y}): {rgb}')
new_rgb=(255,0,0)
image.putpixel((x,y),new_rgb)
output_path='/home/rguktrkvalley/computational lab/week8/1701322810442.png'
image.save(output_path)
image.close()
