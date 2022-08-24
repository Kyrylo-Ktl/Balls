## Visualization of the mathematical model of perfectly elastic collision

$$dist=\sqrt{(x_{1}-x_{2})^{2}+(y_{1}-y_{2})^{2}}$$

$$n_{x}=\frac{x_{2}-x_{1}}{dist}$$

$$n_{x}=\frac{x_{1}-x_{2}}{dist}$$

$$t_{x}=-n_{y}$$

$$t_{y}=n_{x}$$

$$dpn_{1}=v_{1x}*n_{x}+v_{1y}*n_{y}$$

$$dpn_{2}=v_{2x}*n_{x}+v_{2y}*n_{y}$$

$$m_{1} = \frac{dpn_{1} * (mass_{1} - mass_{2}) + 2*mass_{2}*dpn_{2}}{mass_{1}+mass_{2}}$$

$$m_{1} = \frac{dpn_{2} * (mass_{2} - mass_{1}) + 2*mass_{1}*dpn_{1}}{mass_{1}+mass_{2}}$$
