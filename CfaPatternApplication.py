__author__ = "Sneha Sudhakaran"
__copyright__ = "Copyright"
__license__ = "N/A Not licensable"
__status__ = "Production"

from PIL import Image
import numpy as np
import filter_functions as fil_func
import generic_functions as gen_func

num_pictures=12
for picture in range(1,num_pictures):
    filepath="images\\group\\"+str(picture)+".jpg"
    photo = Image.open(filepath)
    images=[]
    images.append(photo)
    photo = photo.convert('RGB')
    rgb_array=np.array(photo)
    w = int(photo.size[0])
    h = int(photo.size[1])
    filter_types=["XTRANS","CYYM","BAYER","RRGB","BAYER_QUAD","RYYB","RGBW_BAYER","RGBW_BAYER_1","RGBW_BAYER_2","RGBW_BAYER_3","CYYM","CYGM","RWWW","RWWB"] # "RYYB_QUAD_BAYER","RYYB",

    for t in range(len(filter_types)):
        CFA_pattern=filter_types[t]
        new_array=rgb_array.copy()
        filter_ref=rgb_array.copy()
        new_array,filter_ref = fil_func.apply_pattern(CFA_pattern,new_array,h,w)
        
        image_new = Image.fromarray(new_array,mode="RGB")
        filepath = "images\\group\\" + str(picture) +"_"+ str(filter_types[t])+ ".jpg"
        image_new.save(filepath)
        images.append(image_new)

    print("done")
    filepath="images\\"+str(picture)+"_compare.jpg"
    filters_array= ["ORIG"] + filter_types




