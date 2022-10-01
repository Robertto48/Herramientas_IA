import numpy as np
import matplotlib.pyplot as plt

class PLOT_UN_SQ():
  
  def plot_un_sq(self,e0,e1,e2,e1n,e2n,mycolor):
    e3=e1+e2
    un_sq=np.array([e0,e1,e2,e3])
    vectors_rn = np.array([[*e0, *e1],
                        [*e0, *e2]])
    X0, Y0, Xf, Yf = zip(*vectors_rn)
    ax = plt.gca()
    x_lim=[un_sq.min(axis=0)[0]-1, un_sq.max(axis=0)[0]+1]
    y_lim=[un_sq.min(axis=0)[1]-1, un_sq.max(axis=0)[1]+1]
  #  print(x_lim); print(y_lim)
    
    ax.quiver(X0, Y0, Xf, Yf, angles='xy', scale_units='xy',
            color=[mycolor,mycolor],scale=1)
    #ax.annotate(e1n + f'({e1[0]},{e1[1]})', (e1[0],e1[1]),fontsize=14)
    #ax.annotate(e2n + f'({e2[0]},{e2[1]})', (e2[0],e2[1]),fontsize=14)
    bx1=[e0[0],e1[0],e3[0]]
    bx2=[e0[0],e2[0],e3[0]]
    by1=[e0[1],e1[1],e3[1]]
    by2=[e0[1],e2[1],e3[1]]
    plt.fill(
      np.append(bx1, bx2[::-1]),
      np.append(by1, by2[::-1]), 
      mycolor, alpha=0.2)
    ax.set_xlim(x_lim);ax.set_ylim(y_lim)
