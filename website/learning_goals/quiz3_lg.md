**Quiz 3 Learning goals**

Our third quiz is scheduled for Thursday, March 14th. It will be 30
minute in pen and paper format. Bring a calculator. The learning goals
for this quiz are:

Differential equations

1\. Be able to take a discrete approximation to limit of infinitesimal
volume size and time step to arrive at the partial differential
equation.  
2\. Partial differential equation:  
   - distinguish between terms that represent fluxes, sources and
storage of quantities within the volume (infinitesimal point).  
   - recognize the order of the equation.  
   - recognize conservative forms

   - be able to write the steady-state version of a PDE

   - be able to understand the significance of the mathematical concept
of divergence and its relationship to flux at a point

   - be able to recognize a partial differential equation when written
in vector form using divergence and gradient and “nabla” notation.

   - be able to analyze units

   - be able to predict the asymptotic solutions of simple boundary
value problems

   - give a physical interpretation of a PDE  
   - be able to simplify a partial differential equation when
coefficients are constant.

    
3\. Be able to set up boundary value problem:  
   - define domain of the problem.  
   - define the equations that govern the dependent variable.  
   - define the parameters of the equation, and if they are spatially
homogeneous (do not vary in space) or heterogeneous.

 

Simulation / python

  
1\. Be able to read a code fragment in python (to the level covered in
the notebooks given in class up to March 12, 2019), and recognize syntax
errors, or predict the result of simple short functions.

2\. Be able to define a simple class that contains class variables,
instance variables and instance methods and use it to pass parameters
into and out of a function.

3\. Be able to write basic functions with default values (similar than
quiz 2)


For the mathematical/physical/pde concepts, refer to the notebook
<https://phaustin.github.io/eosc213/web_notebooks/9_pdes_1.html>

\- understand the conservation/continuity equation (equations
13,24,27,28,31). Be able to explain what it means, what are the
different terms, ... If **provided** with certain fluxes, be able to
know the units (diffusion coefficient, darcy-velocity, heat fluxes, ...
for example).

\- be able to manipulate this equation (write it with nabla, divergence,
gradient, ... be able to specify it in 1D, 2D, steady-state, ...) and
simplify it if certain assumptions are given.

\- understand concepts of divergence, fluxes

\- understand the link between the PDE and the stencil (how to
approximate the derivatives of the fluxes based on discrete
approximation: west-center-east).

\- if given certain boundary conditions in certain problem, be able to
conceptually draw the steady-state solution.

 

For concrete examples to practise and understand the different
influences of boundary conditions, solution profiles, the 1d transient
assignment or the different notebooks we have covered should really help
you. Run these programs, modify boundary conditions. You can do the same
with the first part of the 2d transient assignement (it includes
multiple types of boundary conditions, can deal with heterogeneities,
source terms). You can play around to understand the link between
boundary conditions and steady-state solutions and build your intuition.

 

For the Python questions:

\- check out last quiz: you should be able to do that question

\- the notebooks about classes today: you should be able to predict the
value "30" which was asked in class. And to add a function(method) in
the class.

 

For the classes, the example given today in class (or in 2D assignment)
can help you with that. For function practise, try to develop your own
function. Look at the function "harmonic averaging" of the 2D transient
assignement and modify it to a geometric or arithmetic averaging. You
can take any simple problem you want and put it in a function (absolute
value, square, opposite, ...) for good practise. We learn coding by
coding\!

 
