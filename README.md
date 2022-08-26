# Visualization of perfectly elastic collision

The repository contains implementations of the mathematical apparatus and visualization of the absolutely elastic collision of balls with the exchange of kinetic energy in two-dimensional space.

# Running

- ```pip install -r requirements.txt``` - install all needed dependencies
- ```python run.py``` - run visualization and enjoy

# Examples

https://user-images.githubusercontent.com/93226646/186855664-c90cfcb9-bdb0-4fff-8c15-9552903f2e2c.mp4

https://user-images.githubusercontent.com/93226646/186855692-e82ff61b-871c-4ac2-b000-42fadb202c45.mp4

https://user-images.githubusercontent.com/93226646/186855790-e29e69ea-7aee-43ea-86f8-f251c4b8ee8a.mp4

https://user-images.githubusercontent.com/93226646/186855806-d5bc63f3-cf0f-42f4-8be0-cc81c68d796c.mp4

# Model setup

-  ```WIDTH``` and ```HEIGHT``` - field dimensions in pixels;
-  ```N_BALLS``` - the actual number of balls to be added (optimal value is from 0 to 100);
-  ```BALL_MIN_X_SPEED``` and ```BALL_MAX_X_SPEED``` - minimum and maximum initial speed for the ball along the x-axis;
- ```BALL_MIN_Y_SPEED``` and ```BALL_MAX_Y_SPEED``` - minimum and maximum initial speed for the ball along the y-axis;
- ```BALL_MIN_RADIUS``` and ```BALL_MAX_RADIUS``` - minimum and maximum ball radius (I recommend no more than 5% of the field size);
- ```BALL_X_ACCELERATION``` and ```BALL_Y_ACCELERATION``` - initial acceleration along the axes, if **less than 1** then the balls will **slow down** and the system will **lose** energy, if **more than 1** then the balls will **accelerate** and the system will **increase** energy and if **equal to 1** then the balls will move at a **constant speed** and the energy of the entire system will be **unchanged**;
- ```HANDLE_COLLISIONS``` - a boolean indicating that collisions should be handled, when set to ```False``` the balls will fly through each other;
- ```FPS``` - the number of frames per second, optimally 120, but depends on the performance of the hardware.

# Mathematical apparatus

## Ball representation

The mathematical model is two-dimensional, so $x$ and $y$ coordinates are sufficient for representation.\
\
In order to represent the movement of the ball on a plane, we will store the speed along the $x$ axis as $v_{x}$ and the $y$ axis as $v_{y}$, so the total speed is calculated by the formula $v=\sqrt{v_{x}^{2}+v_{y}^{2}}$.\
\
In order for the ball to move in time with different speeds, it is also necessary to store the acceleration along the $x$ axis as $a_{x}$ and the $y$ axis as $a_{y}$, so the total acceleration is calculated by the formula $a=\sqrt{a_{x}^{2}+a_{y}^{2}}$.\
\
Also, the ball needs a radius $R$ and a certain mass $m$, which will be calculated by the formula $m=\pi*R^{2}$ (square of the circle with radius $R$).

![ball_representation drawio](https://user-images.githubusercontent.com/93226646/186864652-6ad8a0a0-c247-40d3-a101-1cbd8792b46b.png)

## Ball moving

To move the ball, it is necessary to recalculate the coordinates and accelerations along axes in t seconds using the following formulas:

$$x=x+v_{x}*t$$

$$y=y+v_{y}*t$$

$$v_{x}=v_{x}*a_{x}$$

$$v_{y}=v_{y}*a_{y}$$

## Wall collision handling

When colliding with a wall, to reflect the ball from it, it is enough to invert the direction of movement along the corresponding axis:

![wall_collision drawio](https://user-images.githubusercontent.com/93226646/186864820-5f77bfa9-203a-47f3-98a9-3e518c674ba1.png)

## Balls collision

To check whether it is necessary to handle a collision between the balls, it is necessary to estimate the distance between their centers and, if it is less than or equal to the sum of the radii, process the collision. To indicate the overlap of balls (collisions), the following formula is used:

$$dist=\sqrt{(x_{1}-x_{2})^{2}+(y_{1}-y_{2})^{2}}$$

$$eps=10^{-3}$$

$$dist+eps\leq R_{1}+R_{2}$$

![overlap drawio](https://user-images.githubusercontent.com/93226646/186865027-d56747f7-47d3-49f0-bca9-0289821e9f78.png)

If the balls collided (an overlap was detected according to the formula above), then it is necessary to push the balls away from each other and recalculate the corresponding direction vectors and velocities.

![ball_collision drawio](https://user-images.githubusercontent.com/93226646/186864784-b60b9b7b-889e-4d94-a68a-a3367f8f8616.png)

First you need to calculate the normals for the axes:

$$n_{x}=\frac{x_{2}-x_{1}}{dist}$$

$$n_{x}=\frac{x_{1}-x_{2}}{dist}$$

Then the tangents for the axes are calculated:

$$tan_{x}=-n_{y}$$

$$tan_{y}=n_{x}$$

Next, the scalar product of the normals for each axis is calculated:

$$dpn_{1}=v_{1x}*n_{x}+v_{1y}*n_{y}$$

$$dpn_{2}=v_{2x}*n_{x}+v_{2y}*n_{y}$$

Calculate momentum for each axis:

$$p_{1} = \frac{dpn_{1} * (m_{1} - m_{2}) + 2*m_{2}*dpn_{2}}{m_{1}+m_{2}}$$

$$p_{2} = \frac{dpn_{2} * (m_{2} - m_{1}) + 2*m_{1}*dpn_{1}}{m_{1}+m_{2}}$$

We calculate the scalar product of tangents along the axes:

$$dptan_{1}=v_{1x}*tan_{x}+v_{1y}*tan_{y}$$

$$dptan_{2}=v_{2x}*tan_{x}+v_{2y}*tan_{y}$$

And finally we recalculate the speeds for both balls along each axis:

$$v_{1x}=tan_{x}*dptan_{1}+n_{x}*p_{1}$$

$$v_{1y}=tan_{y}*dptan_{1}+n_{y}*p_{1}$$

$$v_{2x}=tan_{x}*dptan_{2}+n_{x}*p_{2}$$

$$v_{2y}=tan_{y}*dptan_{2}+n_{y}*p_{2}$$

## Energy of the whole system

The kinetic energy of each ball is calculated by the following formula:

$$v=\sqrt{v_{x}^2 + v_{y}^2}$$

$$E=m*v^2$$

The total energy of the system is calculated as the sum of the energies of all its balls:

$$totalE = \sum_{i}^{n}E_{i}$$

### System saving energy

https://user-images.githubusercontent.com/93226646/186863474-69715a3a-8f6d-4458-b3b6-d6889514a388.mp4

### System losing energy

https://user-images.githubusercontent.com/93226646/186863382-58fdef32-3192-4e8f-9e76-f70db6e070aa.mp4

### System gaining energy

https://user-images.githubusercontent.com/93226646/186863210-092d40c5-e4c6-4702-b899-3cf6d9d49bc1.mp4
