from scipy import misc
from matplotlib import pyplot as plt
import numpy as np
#get face image of panda from misc package
panda = misc.face()
#plot or show image of face
plt.imshow( panda )
plt.show()
#Flip Down using scipy misc.face image  
flip_down = np.flipud(misc.face())
plt.imshow(flip_down)
plt.show()
