import numpy as np
X=np.array([2,1]).reshape(2,1)
W=np.array([2,2]).reshape(1,2)
class MULGATE:
   def forward(self,X,W):
        return np.dot(X,W)



if __name__=="__main__":
    m=MULGATE(	)
    print(m.forward(X,W).shape)
