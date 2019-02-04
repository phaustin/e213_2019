%file = rflow1.m
%update: 07.10.1996/ILM
%purpose: solve 1D radial flow towards a constant-head well
%         (geology 562,sept 30, 1996)

%--boundary conditions---
H1=8;
H2=10;

%--grid---
deltar=[5,7.5,11.25,16.88,25.27]';   %colomn vector of gridblocks
r0=10;                              %radius at inner boundary

N=length(deltar);     %give the # of gridblocks; length of vector deltar

%--calculate radius to the block interfaces
r = zeros(N,1);     %prelocate r as a column vector
for ir=1:N
  r(ir)=10+sum(deltar(1:ir));
end

%--set up matrix---

A=zeros(N);     % prelocate matrix A

%--elements in the 1st row (influence of boundary)
A(1,1) = -2*(r0+deltar(1)/4)/deltar(1) - 2*r(1)/(deltar(1)+deltar(2));
A(1,2) = 2*r(1)/(deltar(1)+deltar(2));

%--elements in the Nth row (influence of boundary)
A(N,N-1) = 2*r(N-1)/(deltar(N-1)+deltar(N));
A(N,N) = -2*r(N-1)/(deltar(N-1)+deltar(N)) -2*(r(N)-deltar(N)/4)/deltar(N);

%-- element in rest of matrix put in row by row
for i=2:N-1
   dr_m=0.5*(deltar(i-1)+deltar(i));
   dr_p=0.5*(deltar(i)+deltar(i+1));
   A(i,i-1:i+1)=[r(i-1)/dr_m,-(r(i-1)/dr_m+r(i)/dr_p),r(i)/dr_p];
end

%--set up vector with boundary condition

H=zeros(N,1);   % prelocate column-vector H

H(1) = -2*(r0+deltar(1)/4)*H1/deltar(1);
H(N) = -2*(r(N)-deltar(N)/4)*H2/deltar(N);

%--solve the system

h = inv(A)*H;

%--exact answer---

rcell=r-0.5*deltar;    %calculate radius at the mid point of the cell

hexact = (H1-H2)*log(rcell)/log(r0/r(N)) + H1 - (H1-H2)*log(r0)/log(r0/r(N));

%--deviation between analytic and numeric solution
deltah=(h-hexact)./hexact;

%-- plot of the solution and exact answer---
subplot(211)
plot(rcell,h,':',rcell,h,'+',rcell,hexact,rcell,hexact,'o')
axis([r0 r(N) H1 H2])
ylabel('head [m]')
xlabel('radius [m]')
title('HEAD: analytical solution(---),  numeric solution (....)')

%-- plot of the deviation---
subplot(212)
plot(rcell,deltah)
ylabel(' deviation')
xlabel('radius [m]')
title('HEAD: deviation between analytical and numeric solution')

%endfile rflow1.m
