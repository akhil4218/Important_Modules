import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")    #back ground color
# style.use("fivethirtyeight")  waste when compared to ggplot
# If u set program to plot both graphs and bars then it does both on seperate tabs
#>>> list of colors   r->red k->black g->green  b->blue  c->I can't figure it out

"""
plt.plot([1,2,3],[4,5,6],label="first",color="r",linewidth=2)    
plt.plot([11,12,13],[14,15,16],label="Second",color="k",linewidth=2)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.legend(loc=4)    #    if loc=0  -> top left if 1 top right if 3 bottom left if 4 bottom right
# above will prints label names in top right (or) left corner
plt.grid(True,color="b")    #blackground lines
plt.title("GRAPH")
#plt.savefig("akhil.png")  # to save plot images
plt.show()
# <- NOTE ->  plt.plot(x,y,"o")  wil  plot with big dots
"""

"""
#>>> BARS

x=[11,22,33]
y=[55,77,99]
a=[21,31,41]
b=[44,66,88]
plt.bar(x,y,label="first",color="c")   #len(s)==len(y)  Mandatory
plt.bar(a,b,label="second",color="b")
plt.show()
"""



#>>>histograms  diff b/w bars and histograms  in bars length of lists should be equal but in histograms we can make difference
x=[11,12,13,14,115,16,21,22,23,24,25,31,32,33,34,35]
y=[0,5,10,15,20,25,30,35,40]   # always it should be in incresing order only
plt.hist(x,y,histtype="bar",rwidth=0.1,color="r")
plt.show()


"""
#>>> scatter  points
xx=[2,5,8]
yy=[33,55,88]
plt.scatter(xx,yy,marker="o",color="g")    #marker means symbol   #type of markers "o"  ,   "+"  ,  "*"
plt.show()
"""

"""
#>>> pie
q=[1,2,3,4,5]
w=[13,76,34,90,54]
e=[22,33,44,55,66]
r=[32,43,54,65,76]
#plt.subplot(211)    #  first no says there are 2 graphs and second sas
plt.plot([],[],label="first",color="r")
plt.plot([],[],label="second",color="b")
plt.plot([],[],label="third",color="g")
plt.stackplot(q,w,e,r)
plt.legend()
plt.show()
"""



#>>>
a=[20,30,70]
activities=["first","second","third"]
col=["r","b","g"]
#plt.subplot(212)
plt.pie(a,labels=activities,colors=col,startangle=90,explode=(0,0.2,0),autopct="%1.0f%%")  # remember
plt.show()



"""
import numpy
img=numpy.random.rand(50,50)   #(hieght,width)
plt.imshow(img)
#plt.gray()   # in black and white
#plt.figure()
plt.pcolor(img)
plt.hot()
plt.colorbar()  # shows color bar
plt.show()
"""
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)

plt.plot(x, y)
plt.plot(x, y,'r')
plt.grid()
#plt.ﬁgure()
"""
"""
image = np.random.rand(30, 30)
plt.imshow(image)
plt.gray()
plt.ﬁgure()
plt.pcolor(image)
plt.hot()
plt.colorbar()

plt.show()

"""

#   -----> 3D ploting
"""

from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)
#ax=fig.add_subplot(111,projection="3d")
x=[11,12,13,14,15]
y=[15,32,53,74,15]
z=[71,42,23,33,25]
ax.plot(x,y,z)    #  plot or scatter
plt.show()

"""














