"""
Software to define and save colormaps for Gravbox, an Augmented Reality Gravitational Dynamics Simulation. 

This was developed at the University of Iowa by Jacob Isbell
    based on work in Dr. Fu's Introduction to Astrophysics class by Jacob Isbell, Sophie Deam, Jianbo Lu, and Tyler Stercula (beta version)
Version 1.0 - December 2017
"""


import numpy as np

def mk_jet():
       #[r,g,b,opacity]
       cmap = np.array([[ 0         ,  0.        , 0.         ,  1.        ],[ 0.        ,  0.        ,  0.5       ,  1.        ],
              [ 0.        ,  0.        ,  1.        ,  1.        ],
              [ 0.        ,  0.38888889,  1.        ,  1.        ],
              [ 0.        ,  0.83333333,  1.        ,  1.        ],
              [ 0.3046595 ,  1.        ,  0.66308244,  1.        ],
              [ 0.66308244,  1.        ,  0.3046595 ,  1.        ],
              [ 1.        ,  0.90123457,  0.        ,  1.        ],
              [ 1.        ,  0.48971193,  0.        ,  1.        ],
              [ 1.        ,  0.0781893 ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0.5       ,  0.        ,  0.        ,  1.        ],
              [ 0         ,  0.        , 0.         ,  1.        ] #black levels for contours
              ])

       np.save('cmap_jet.npy', cmap)


def mk_sauron():
       red =   [0.0, 0.0,.2, 0.4,  0.5, 0.3, 0.0, 0.7, 1.0, 1.0,  1.0, 0.9]
       green = [0.0, 0.0,.42, 0.85, 1.0, 1.0, 0.9, 1.0, 1.0, 0.85, 0.0, 0.9]
       blue = [0.0, 1.0,1., 1.0, 1.0, 0.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9]

       sauron = []
       for k in range(len(red)):
              #[r,g,b,opacity]
              sauron.append([red[k],green[k], blue[k], 1.])
       sauron.append([0,0,0,1.]) #black level for contours

       np.save('cmap_sauron.npy', np.array(sauron))

def mk_viridis():
       #[r,g,b,opacity]
       v = np.array([[ 68,   1,  84, 255],
       [ 72,  21, 103, 255],
       [ 72,  38, 119, 255],
       [ 69,  55, 124, 255],
       [ 64,  71, 136, 255],
       [ 57,  86, 140, 255],
       [ 51,  99, 141, 255],
       [ 45, 112, 142, 255],
       [ 40, 125, 142, 255],
       [ 35, 138, 141, 255],
       [ 31, 150, 139, 255],
       [ 32, 163, 135, 255],
       [ 60, 187, 117, 255],
       [ 85, 198, 103, 255],
       [115, 208,  85, 255],
       [149, 216,  64, 255],
       [184, 272,  41, 255],
       [220, 227,  25, 255],
       [253, 231,  37, 255],
       [  0,   0,   0, 255]#black for contours
       ]) / 255. 

       np.save('cmap_viridis.npy',v)

def mk_geo():  
       #[r,g,b,opacity]
       v = np.array([[0, 0, 255,255],
              [0, 0, 100,255],
       [ 0, 30, 100,255],
       [ 0, 50, 102,255],
       [19, 108, 160,255],
       [24, 140, 205,255],
       #[135, 206, 250,255],
       #[176, 226, 255,255],
       [0, 97, 71,255],
       [16, 122, 47,255],
       [232, 215, 125,255],
       [161, 67, 0,255],
       [130, 30, 30,255],
       [145, 80, 80,255],
       [161, 161, 161,255],
       [206, 206, 206,255],
       [255, 255, 255,255],
       [0,0,0,255] #black levels for contours
       ]) /255.
       np.save('cmap_geo.npy',v)    

       #remember that spacing isnt linear [-40,-30,-20,-12.5,-.75,-.25,-.05,0,.05,.25,.75,12.5,20,30,40]
if __name__ == '__main__':
       mk_jet()
       mk_viridis()
       mk_sauron()
       mk_geo()

