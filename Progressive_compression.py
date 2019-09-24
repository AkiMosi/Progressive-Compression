from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def progressive(pixel,count):
    mat = []
    for i in range(2**(count-1)):
        temp = []
        for j in range(2**(count-1)):
            temp.append(np.array([0,0,0]))
        mat.append(temp)
    mat = np.array(mat)
    im_new = Image.new(im.mode,[len(mat),len(mat)])
    pixel_new = im_new.load()
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i,j][0] = (pixel[2*i,2*j][0]+pixel[(2*i)+1,2*j][0]+pixel[2*i,(2*j)+1][0]
                        +pixel[(2*i)+1,(2*j)+1][0])/4
            mat[i,j][1] = (pixel[2*i,2*j][1]+pixel[(2*i)+1,2*j][1]+pixel[2*i,(2*j)+1][1]
                        +pixel[(2*i)+1,(2*j)+1][1])/4
            mat[i,j][2] = (pixel[2*i,2*j][2]+pixel[(2*i)+1,2*j][2]+pixel[2*i,(2*j)+1][2]
                        +pixel[(2*i)+1,(2*j)+1][2])/4
            pixel_new[i,j] = tuple(mat[i,j])
    stri = "layer"+str(count)+".jpg"
    im_new.save(stri)
    strit = "layer"+str(count)+"*"+str(count)
    plt.title(strit)
    plt.imshow(im_new)
    plt.show()
    return mat

im = Image.open('color1.jpg')
i = 2
count = 0
flow = []
flow_count = 0
while(i < im.size[0]):
    i *= 2
    count += 1
i /= 2
im = im.resize([int(i),int(i)])

pixel_map = im.load()
pixel = []
for i in range(im.size[0]):
    temp = []
    for j in range(im.size[0]):
        temp.append(pixel_map[i,j])
    pixel.append(temp)
pixel = np.array(pixel)
flow.append(pixel)

while(count>0):
    flow.append(progressive(flow[flow_count],count))
    flow_count += 1
    count -= 1

