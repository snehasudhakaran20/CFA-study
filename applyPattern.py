__author__ = "Sneha Sudhakaran"
__copyright__ = "Copyright"
__license__ = "N/A Not licensable"
__status__ = "Production"

from unittest import case
import numpy as np

def apply_pattern(pattern_type,new_pixel_array,h,w):

    pattern,size=choose_pattern(pattern_type)
    filter_pattern_ref=new_pixel_array.copy()

    def convert_xyto_pos(x,y,size):
        pos = (x%size)*size+(y%size)
        return pos

    def str_to_rgb(A):
        match(A):
            case 'R':
                rgb=[255,0,0]
            case 'G':
                rgb=[0,255,0]
            case 'B':
                rgb=[0,0,255]
            case 'W':
                rgb=[255,255,255]
            case 'C':
                rgb=[0,255,255]
            case 'Y':
                rgb=[255,255,0]
            case 'M':
                rgb=[255,0,255]
        return rgb

    def apply_mask(pixel,rgb_mask):
        r,g,b=rgb_mask
        #print(r,g,b)

        r0,g0,b0=pixel.copy()
        if(r==0):
            r0=0
        else :
            r0=int(pixel[0])
        if(g==0):
            g0=0
        else:
            g0=int(pixel[1])
        if(b==0):
            b0=0
        else:
            b0=int(pixel[2])

        pixel_new=[r0,g0,b0]
        #print("new pixel")
        #print(pixel_new)
        return pixel_new

    len_=len(new_pixel_array)
    #print(len_)
    #print(w)
    #print(h)
    for y in range(0, h):
        for x in range(0, w):
            pos=convert_xyto_pos(x, y,size)
            #print(pos)
            #print(filter_pattern_ref[x][y])
            filter_pattern_ref[y][x] = str_to_rgb(pattern[pos])
            new_pixel_array[y][x] = apply_mask(new_pixel_array[y][x], filter_pattern_ref[y][x])

    return new_pixel_array,filter_pattern_ref

def choose_pattern(pattern_type):

    print(pattern_type)

    G='G'
    B='B'
    R='R'
    W='W'
    C='C'
    Y='Y'
    M='M'

    match pattern_type:
        case "BAYER_QUAD" :
            pattern = [G, G, R, R,
                       G, G, R, R,
                       B, B, G, G,
                       B, B, G, G]
            size=4

        case "RGBW_BAYER" :
            pattern = [W, R, W, R,
                       B, G, B, G,
                       W, R, W, R,
                       B, G, B, G]
            size=4

        case "RGBW_BAYER_1":
            pattern = [W, B, W, G,
                       B, W, G, W,
                       W, G, W, R,
                       G, W, R, W]
            size = 4

        case "RGBW_BAYER_2":
            pattern = [G, W, R, W,
                       G, W, R, W,
                       B, W, G, W,
                       B, W, G, W]
            size = 4

        case "RGBW_BAYER_3":
            pattern = [G, W, R, W,
                       B, W, G, W,
                       G, W, R, W,
                       B, W, G, W]
            size = 4

        case "QUAD_BAYER":
            pattern = [G, G, R, R,
                       G, G, R, R,
                       B, B, G, G,
                       B, B, G, G]
            size = 4

        case "RYYB_QUAD_BAYER":
            pattern = [Y, Y, R, R,
                       Y, Y, R, R,
                       B, B, Y, Y,
                       B, B, Y, Y]
            size = 4
        case "RRGB" :
            pattern = [R, B,
                       G, R ]
            size=2
        case "BAYER" :
            pattern = [G, B,
                       R, G ]
            size=2

        case "RYYB" :
            pattern = [Y, R,
                       B, Y ]
            size=2

        case "CYYM" :
            pattern = [C, Y,
                       Y, M ]
            size=2

        case "CYGM" :
            pattern = [C, Y,
                       G, M ]
            size=2

        case "XTRANS":
            pattern = [G, B, G, G, R, G,
                       R, G, R, B, G, B,
                       G, B, G, G, R, G,
                       G, R, G, G, B, G,
                       B, G, B, R, G, R,
                       G, R, G, G, B, G]
            size=6

        case "RWWW":
            pattern = [R, W,
                       W, W ]
            size=2

        case "RWWB":
            pattern = [R, W,
                       W, B ]
            size=2

        case "CYYM":
            pattern = [G, B, G, G, R, G,
                       R, G, R, B, G, B,
                       G, B, G, G, R, G,
                       G, R, G, G, B, G,
                       B, G, B, R, G, R,
                       G, R, G, G, B, G]
            size=6

        case "NORED":
            pattern = [C]
            size=1

        case "NOBLUE":
            pattern = [Y]
            size = 1

        case "NOGREEN":
            pattern = [M]
            size = 1

        case _:
            pattern = [G, B, G, G, R, G,
                       R, G, R, B, G, B,
                       G, B, G, G, R, G,
                       G, R, G, G, B, G,
                       B, G, B, R, G, R,
                       G, R, G, G, B, G]
            size=0

    return pattern,size




