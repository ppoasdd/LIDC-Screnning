import numpy as np
from matplotlib import pyplot, cm

def plotArray(testimage,xrange,yrange):
    l1=np.arange(xrange)
    l2=np.arange(yrange)
    fig=pyplot.figure()
    pyplot.axes().set_aspect('equal', 'datalim')
    pyplot.set_cmap(pyplot.gray())
    pyplot.pcolormesh(l1, l2, np.flipud(testimage))
    pyplot.axis('scaled')
    pyplot.show()
    pyplot.close()
	
def plotArrayWithbBox(testimage,xrange,yrange,xCoord,yCoord,size=50):
    l1=np.arange(xrange)
    l2=np.arange(yrange)
    fig=pyplot.figure()
    pyplot.axes().set_aspect('equal', 'datalim')
    pyplot.set_cmap(pyplot.gray())
    pyplot.pcolormesh(l1, l2, np.flipud(testimage))
    
    for i in range(len(xCoord)):
        rectangle = pyplot.Rectangle((yCoord[i]-size/2, 512-(xCoord[i]+size/2)), size, size, fill=False, color='r')
        pyplot.gca().add_patch(rectangle)
    
    pyplot.axis('scaled')
    pyplot.show()
    pyplot.close()

def plotArrayWithbBoxSave(testimage,testnumber,xrange,yrange,xCoord,yCoord,size=50):
    l1=np.arange(xrange)
    l2=np.arange(yrange)
    fig=pyplot.figure()
    pyplot.axes().set_aspect('equal', 'datalim')
    pyplot.set_cmap(pyplot.gray())
    pyplot.pcolormesh(l1, l2, np.flipud(testimage))
    
    for i in range(len(xCoord)):
        rectangle = pyplot.Rectangle((yCoord[i]-size/2, 512-(xCoord[i]+size/2)), size, size, fill=False, color='r')
        pyplot.gca().add_patch(rectangle)
    
    pyplot.axis('scaled')
    fig.savefig('G:/Jupyter_python/Beom/170214/screening samples/top10diff/'+str(testnumber+1)+'.png')
    pyplot.close()