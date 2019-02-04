c %G% %W%
c  *************************************************************************
c  *                                                                       *
c  *                          F l o w s s                                  *
c  *                                                                       *
c  *************************************************************************
c  Programmed by: Roger Beckie
c  Last updated:  Oct. 1997
c
c  Modifications history:
c  Oct. 10/97  - variable grid spacing, red-black sor, heterogeneous
c  Nov. 14/96  - adjust for WATFOR
c  Oct. 31/96  - change array dimensioning conventions
c  Nov. 2/95   - added surfer grid file output capability
c  Nov. 14/94  - corrected for WATFOR
c
c
c  This code solves the steady state, heterogeneous isotropic flow equation
c  of the form: d/dx(Tdh/dx) + d/dy(Tdh/dy) = Q, where h is head, Q is
c  pumping and leakage fluxes, and T is the transmissivity.
c
c  Method
c  ======
c  This code uses a basic cell centered finite difference formulation
c  with an SOR solver.
c
c  Inputs
c  ======
c  The code is run from a control file named flowss.con.
c  The control file contains some basic parameters, and the names of
c  other input and output files. See the subroutine INPUTS for information
c  on the inputs required to run the code.
c
c
c  Variables
c ===========
c h(i,j)  head at point i, j on grid, where i indexes the x direction and j
c         indexes the y direction.
c q(i,j)  leakage and pumping in gridblock i,j (expressed as vol/area/time)
c
c ind(i,j) integer, if = 1, then a constant head node, otherwise, free node.
c                  
c
c              o N
c ^ y          |
c |          C |            Finite difference stencil for node  i, j
c |   W  o --- o --- o E
c  ----> x     |
c              |
c              o S
c
c The coefficients for the discrete approximation at node i, j are:
c c(i,j)  for the central node of a discrete approximation.
c n(i,j)  for the north node of a discrete approximation.
c s(i,j)  for the south node of a discrete approximation.
c e(i,j)  for the east node of a discrete approximation.
c w(i,j)  for the west node of a discrete approximation.
c trans(i,j) transmissivity at node i, j.
c dx(i), dy(j)  - delta x and delta y in gridblock (i,j).
c ioecho  unit number for general echo of input.
c iohead  unit number for head output file.
c iosurf  unit number for head grid file.
c itmax, omega, tol = max iterations, accel. param. and tolerance for solution.
c
       program flowss
       integer maxx, maxy
       parameter(maxx=31)
       parameter(maxy=31)
       integer  nx, ny, iohead, ioecho, iosurf, itmax, ldi, ldj
       integer ind(maxx, maxy)
c
c      place an extra row of transmissivities to ease assembly of equations
c
       real*8  dx(0:maxx), dy(0:maxy), tol, omega
       real*8  trans(0:maxx+1, 0:maxy+1)
       real*8  c(maxx, maxy), n(maxx, maxy)
       real*8  s(maxx, maxy), e(maxx, maxy)
       real*8  w(maxx, maxy), h(0:maxx+1, 0:maxy+1)
       real*8  q(maxx, maxy), rhs(maxx, maxy)
c
c
c      set lead dimensions of arrays 
       ldi = maxx
       ldj = maxy
c
c      *********************************
c      *                               *
c      *         I n p u t s           *
c      *                               *
c      *********************************
c
c
	call inputs(iohead, ioecho, nx, ny, dx, dy, ind, h, q, trans,
     > itmax, omega, tol, iosurf, ldi, ldj)

c
c
c      *********************************
c      *                               *
c      *   D e f i n e  c o e f f s    *
c      *                               *
c      *********************************
c
c
	call defcoefs(ind, nx, ny, trans, q, dx, dy, c, n,
     >  s, e, w, h, rhs, ldi, ldj)
c
c
c
c      *********************************
c      *                               *
c      *      S O R  S O L V E R       *
c      *                               *
c      *********************************
c
c
	 call sorsolver(ioecho, nx, ny, h, c, n, s, e, w, rhs, itmax,
     >   omega, tol, ldi, ldj)
c
c      *********************************
c      *                               *
c      *         O u t p u t s         *
c      *                               *
c      *********************************
c
c
	call outputs(nx, ny, dx, dy, iohead, h, ldi, ldj)
c
c      *********************************
c      *                               *
c      *         S u r f i t           *
c      *                               *
c      *********************************
c
c
       call surfit(nx, ny, dx, dy, ind, h, iosurf, ldi, ldj)
18      end
c
c  *************************************************************************
c  *                                                                       *
c  *                             i n p u t s                               *
c  *                                                                       *
c  *************************************************************************
c  This subroutine reads in the required data and echos it out. It is
c  assummed that a file named flowss.con exists in the current directory
c  and contains the following:
c  line
c  =====
c 1: nx, ny             - total number of blocks in x and y direction,
c 2: itmax, omega, tol  - maximum number of iterations, sor factor and toler.
c 3: echofile           - echo data to this file.
c 4: dxfile             - file containing dx's and dy's for grid.
c 5: headout            - head solution file name.
c 6: indfile            - indices (1 = const. head, else free node)
c 7: head0file          - initial guess at heads (for const. head nodes,
c                         initial guess = bc).
c 8: qfile              - contains pumping rates and leakage at each node.
c 9: headgrid           - file name of surfer grid file of head (should be
c                         named with extension .grd).
c 10: logtransfile      - filename of log 10 transmissivity file
c
c example flowss.con file:
c
c  30 30 
c  200 1.9 1.e-6
c  test.out
c  dx30x30.in
c  head.out
c  ind30x30.in
c  h30x30.in
c  q30x30.in
c  h30x30.grd
c  lt30x30.in
c
c
c
       subroutine inputs(iohead, ioecho, nx, ny, dx, dy, ind, h,
     > q, trans, itmax, omega, tol, iosurf, ldi, ldj)
c
       integer ldi, ldj, ind(ldi, ldj), itmax, nx, ny, iohead, ioecho, 
     > iosurf
       real*8 trans(0:ldi+1,0:ldj+1), q(ldi, ldj), 
     > h(0:ldi+1, 0:ldj+1), omega, dx(0:*), dy(0:*), tol
c
c      local variables
       real*8 t 
       integer io
c
       character*90 fname
c
c      *********************************
c      *                               *
c      *   C o n t r o l    f i l e    *
c      *                               *
c      *********************************
c
       open(unit = 2, file = 'flowss.con', status='old')
c
c      read grid parameters, then sor parameters, then echo filename.
c
       read(2, *) nx, ny
       read(2, *) itmax, omega, tol
       read(2, '(a)') fname
c
c      give echo file unit number 11
c
       ioecho = 11
       open(unit = ioecho, file = fname)
c
       write(ioecho, 10) nx, ny, itmax, omega, tol, fname
10     format(//,' 2 - D finite difference flow model of the steady',
     > ' state flow equation', ///,
     > ' Inputs:',/,
     > ' nx, ny: ', i3, 1x, i3,/,
     > ' Max number of sor iterations (itmax): ', i5,/,
     > ' SOR acceleration parameter (omega): ', f5.2,/,
     > ' Solution convergence tolerance (tol): ', g8.2,/,
     > ' Name of echo file (this file): ', a)
c
c      *********************************
c      *                               *
c      *        D x    f i l e         *
c      *                               *
c      *********************************
c
c      read dx and dy from file.
c
       io = 20
       read(2, '(a)') fname
       write(ioecho, 12) fname
12     format(' Grid spacing in filename: ', a)
       open(unit = io, file = fname)
       read(io, *) (dx(i), i=1, nx)
       read(io, *) (dy(j), j=1, ny)
       close(io)
c
c      outside row of dx's
c
       dx(0) = dx(1)
       dx(nx+1) = dx(nx)
       dy(0) = dy(1)
       dy(ny+1) = dy(ny)
c
c      echo gridspacing to echo file

       write(ioecho, 17)
       write(ioecho, 18) (i, dx(i), i=1, nx)
       write(ioecho, 18) (j, dy(j), j=1, ny)
17     format(//, ' Grid spacing: dx then dy ')
18     format((5(i3, 1x, g10.4,1x),/))

c      *********************************
c      *                               *
c      *      H e a d   f i l e        *
c      *                               *
c      *********************************
c
c
c      give head output file unit number 12
c
       iohead = 12
       read(2, '(a)') fname
       write(ioecho, 15) fname
15     format(' Head ouput filename: ', a)
       open(unit = iohead, file = fname)
c
c
c      *********************************
c      *                               *
c      *        I n d   f i l e        *
c      *                               *
c      *********************************
c
c
       read(2, '(a)') fname
       write(ioecho, 20)  fname
20     format(' Index filename: ', a)
       io = 10
       open(unit = io, file = fname)
       call readind(io, ind, nx, ny, ldi, ldj)
c
c      *********************************
c      *                               *
c      *     H e a d 0  f i l e        *
c      *                               *
c      *********************************
c
c
       read(2, '(a)') fname
       write(ioecho, 30)  fname
30     format(' Initial heads filename: ', a)
       open(unit = io, file = fname)
       call readhead(io, h, nx, ny, ldi, ldj)
c
c      *********************************
c      *                               *
c      *          Q  f i l e           *
c      *                               *
c      *********************************
c
c
       read(2, '(a)') fname
       write(ioecho, 40)  fname
40     format(' Fluxes and pumping filename: ', a)
       open(unit = io, file = fname)
       call readq(io, q, nx, ny, ldi, ldj)
c
c      *********************************
c      *                               *
c      *     s u r f e r    g r i d    *
c      *            f i l e            *
c      *                               *
c      *********************************
c 
       iosurf = 15
       read(2, '(a)') fname
       write(ioecho, 50) fname
50     format(' Surfer grid filename: ', a)
       open(unit = iosurf, file = fname)
c
c      *********************************
c      *                               *
c      *       s e t  t r a n s        *
c      *                               *
c      *********************************
c
c
       io = 20
       read(2, '(a)') fname
       write(ioecho, 60) fname
60     format(' Log 10 transmissivity filename: ', a)
       open(unit = io, file = fname)
       call settrans(io, nx, ny, trans, ind, ldi, ldj)
       close(io)
c
c
       return
       end
c  *************************************************************************
c  *                                                                       *
c  *                         r e a d i n d                                 *
c  *                                                                       *
c  *************************************************************************
c  This routine opens and reads a file containing nx x ny integers. The
c  integers must be stored such that ind(1,1) is first, then ind(2,1) etc.
c
c   io = unit number of file (opened)
c   nx, ny = dimensions of field
c
c  *************************************************************************
       subroutine readind(io, ind, nx, ny, ldi, ldj)
       integer io, nx, ny, ldi, ldj, ind(ldi, ldj)
c
       integer i, j
c
       read(io, *) ((ind(i,j), i = 1, nx), j = 1, ny)
c
       close(io)
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                         r e a d h e a d                               *
c  *                                                                       *
c  *************************************************************************
c  This routine opens and reads a file containing nx x ny real*8 and stores
c  them in a matrix with leading dimension nx. The reals*8 must be stored
c  such that h(1,1) is first, then h(2,1) etc.
c
c   io = unit number of file (opened)
c   nx, ny = dimensions of field
c
c  *************************************************************************
       subroutine readhead(io, h, nx, ny, ldi, ldj)
       integer io, nx, ny, ldi, ldj
       real*8 h(0:ldi+1, 0:ldj+1)
c
       integer i, j
c
c      satisfy watfor by initializing all data to zero
c
      do 10, j=0, ny+1
      do 10, i=0, nx+1
	 h(i,j) =0.0
10    continue
       read(io, *) ((h(i,j), i = 1, nx), j = 1, ny)
c
       close(io)
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                         r e a d q                                     *
c  *                                                                       *
c  *************************************************************************
c  This routine opens and reads a file containing nx x ny real*8 and stores
c  them in a matrix with leading dimension nx. The reals*8 must be stored
c  such that h(1,1) is first, then h(2,1) etc.
c
c   io = unit number of file (opened)
c   nx, ny = dimensions of field
c
c  *************************************************************************
       subroutine readq(io, q, nx, ny, ldi, ldj)
       integer io, nx, ny, ldi, ldj
       real*8 q(ldi, ldj)
c
       integer i, j
c
c      satisfy watfor by initializing all data to zero
c
      do 10, j=1, ny 
      do 10, i=1, nx
	 q(i,j) =0.0
10    continue
       read(io, *) ((q(i,j), i = 1, nx), j = 1, ny)
c
       close(io)
       return
       end
c
c
c  *************************************************************************
c  *                                                                       *
c  *                           d e f c o e f  s                            *
c  *                                                                       *
c  *************************************************************************
c  This code determines the coefficients for the discrete approximation
c  for every node in the grid. Constant head nodes are given trivial
c  equations.
c
       subroutine defcoefs(ind, nx, ny, trans, q, dx, dy, c, n,
     > s, e, w, h, rhs, ldi, ldj)
c
       integer nx, ny, ind(ldi,*)
       real*8 condc, dx(0:ldi+1), dy(0:ldj+1), trans(0:ldi+1, 0:ldj+1)
       real*8 c(ldi, *), n(ldi,*), s(ldi, *), e(ldi,*), w(ldi,*)
       real*8 h(0:ldi+1,0:*), rhs(ldi, ldj), q(ldi,*)
c
c      local variables
c
       integer i, j
       real*8 cxp, cxm, cyp, cym
c
c
       do 10, j = 1, ny
	do 10, i = 1, nx
	if((ind(i,j).eq.1).or.(ind(i,j).eq.-1)) then
c
c         trivial equation for constant head node
c
	  c(i,j) = 1.0
	  n(i,j) = 0.0
	  s(i,j) = 0.0
	  e(i,j) = 0.0
	  w(i,j) = 0.0
	  rhs(i,j) = h(i,j)
c
	else
c
	 cxp = condc(trans(i+1,j), trans(i,j), dx(i+1), dx(i))
     >   * dy(j)* 2.0/(dx(i)+dx(i+1))
	 cxm = condc(trans(i-1,j), trans(i,j), dx(i-1), dx(i))
     >   * dy(j)* 2.0/(dx(i)+dx(i-1))
	 cyp = condc(trans(i,j+1), trans(i,j), dy(j+1), dy(j))
     >   * dx(i)* 2.0/(dy(j)+dy(j+1))
	 cym = condc(trans(i,j-1), trans(i,j), dy(j-1), dy(j))
     >   * dx(i)* 2.0/(dy(j)+dy(j-1))
	 c(i,j) = (-(cxp + cxm) - (cyp+cym))
	 n(i,j) = cyp
	 s(i,j) = cym
	 e(i,j) = cxp
	 w(i,j) = cxm
	 rhs(i,j) =  dx(i) * dy(j) * q(i,j)
       endif
10    continue
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                           c o n d c                                   *
c  *                                                                       *
c  *************************************************************************
c  Note that this routines returns the harmonic average for variable spaced 
c  meshes.
       double precision function condc(t1, t2, dx1, dx2)
       real*8 t1, t2, dx1, dx2
       condc = t1*t2*(dx1+dx2)/(t1*dx2 + t2*dx1)
c
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                          s e t t r a n s                              *
c  *                                                                       *
c  *************************************************************************
c  This routine sets up the transmissivity matrix. A buffer of t = 0
c  is placed around the field to allow for easy treatment of no-flow
c  boundary conditions. 
c   nx, ny = dimensions of field
c   trans(i,j) nx x ny matrix of transmissivities, surrounded by one block
c   of transmissivity = 0.0.
c   note at dummy nodes (ind = -1) T is set to zero ===> dummy nodes are 
c   no-flow 
c
c  *************************************************************************
       subroutine settrans(io, nx, ny, trans, ind, ldi, ldj)
       integer  io, nx, ny, ind(ldi, ldj)
       real*8 trans(0: ldi+1, 0:*)
c
       integer i, j
c
c      initialize everything to zero
c
       do 10, j=0, ny+1
	do 10, i=0, nx+1
	 trans(i,j) = 0.0
10     continue
c
c     set interior to default value, set dummy nodes to T=0
c
       read(io,*) ((trans(i,j), i=1,nx),j=1,ny)
       do 20, j=1, ny
	do 20, i=1, nx
	 trans(i,j) = 10**(trans(i,j))
	 if(ind(i,j).eq.-1) trans(i,j) = 0.0
20     continue
c
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                          s o r s o l v e r                            *
c  *                                                                       *
c  *************************************************************************
c  This routine uses SOR to solve the system of equations defined by
c  the coeffients of the computational molecule:
c
c
c              o N
c ^ y          |
c |          C |            Finite difference stencil for node  i, j
c |   W  o --- o --- o E
c              |               ----> x
c              |
c              o S
c
c
c nx, ny = size of grid
c h = current guess at head solution
c c, n, s, e, w, q = coefficients for equation
c itmax = on entry = max number of iterations, on exit, = number of iterations
c omega = acceleration factor
c tol = solution tolerance, ||r(k)||/ ||rhs|| < tol
c ==========================================================================
c Upon reading in the conductivities (or, transmissivities) the
c values are rescaled by dividing through by the geometric mean.
c Thus the new mean value is one.
c
c
       subroutine sorsolver(ioecho, nx, ny, h, c, n, s, e, w, rhs,
     > itmax, omega, tol, ldi, ldj)
       integer nx, ny, itmax, ioecho
       real*8 h(0:ldi+1,0:*), c(ldi,*), n(ldi,*), s(ldi,*), e(ldi,*)
       real*8 omega, tol, w(ldi,*), rhs(ldi,*)
c
c      local variables
c
       integer i, j
       real*8 dh, h0, hg, res
c
c      find h0, norm of initial residual, use in convergence criteria
c
       h0 = 0.0
       do 10, j=1, ny
	do 10, i=1,nx
	 res =
     >         rhs(i,j)
     >       - w(i,j) * h(i-1,j)
     >       - e(i,j) * h(i+1,j)
     >       - n(i,j) * h(i,j+1)
     >       - s(i,j) * h(i,j-1) 
     >       - c(i,j) * h(i,j)
         h0 = h0 + abs(res)
10     continue
c
      write(ioecho, 22)
22    format(' It. #    Convergence')
c
c     now iterate
c
       it = 1
15     continue
c
c
       dh = 0.0
       do 20, j=1, ny
	do 20, i=1, nx
	 res =
     >         rhs(i,j)
     >       - w(i,j) * h(i-1,j)
     >       - e(i,j) * h(i+1,j)
     >       - n(i,j) * h(i,j+1)
     >       - s(i,j) * h(i,j-1) 
     >       - c(i,j) * h(i,j)
         dh = dh + abs(res)
c
c       now do relaxation step
c
	h(i,j) = h(i,j) + omega * res/c(i,j)
20     continue
c
c      now check if converged
       write(ioecho, 25)  it, abs(dh/h0)
25     format( i6, 1x, e13.5)
c
       if(abs(dh/h0).lt.tol) goto 50
c
c      do another iteration or quit
c
       if(it.lt.itmax) then
	 it = it + 1
	 goto 15
       else
c
c      failed to converge
c
	 write(ioecho, 30) it
30       format(' Failed to converge after: ', i6, ' iterations.')
       endif
c
50     continue
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                           o u t p u t s                               *
c  *                                                                       *
c  *************************************************************************
c  This routine is used to output all the solutions to  unformatted files
c  using the standard output protocol accepted by the iris routines.
c
       subroutine outputs(nx, ny, dx, dy, iout, h, ldi, ldj)
c
       integer nx, ny, iout, ldi, ldj
       real*8 h(0:ldi+1,0:*), dx(0:ldi+1), dy(0:ldj+1)
       y=dy(1)/2.
       do 20, j=1, ny
        x = dx(1)/2.
        do 15, i=1,nx
        write(iout, 10) x, y, h(i,j)
        x = x + 0.5*(dx(i)+ dx(i+1))
10      format(g10.4, 1x, g10.4, 1x, e14.7)
15     continue
       y=y+0.5*(dy(j)+dy(j+1))
20     continue
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                            s u r f i t                                *
c  *                                                                       *
c  *************************************************************************
c  This routine is used to output the results to a surfer grid file. The
c  routine uses the index file to determine surfer blank values =0.170141e+39
c  This surfer file only works if the grid is not distorted!
c
      SUBROUTINE surfit(nx, ny, dx, dy, ind, h, io, ldi, ldj)
C
       integer nx, ny, io, ldi, ldj, ind(ldi, *)
       real*8 dx, dy, blank, hmax, hmin,  h(0:ldi+1,0:*)
c
c      define surfer blank value (will not be contoured)
c
       blank=0.170141e+39
c
c      if index is less than zero, set head to blank value
c
       hmax = h(1,1)
       hmin = h(1,1)
       do 5, j=1, ny 
        do 5, i=1, nx
         hmax = max(hmax, h(i,j))
         hmin = min(hmin, h(i,j))
         if(ind(i,j).lt.0) h(i,j)=blank
5      continue
c
c      now print out the header for the surfer grid file
c
       write(io,10) 'DSAA'
10     format(a4)
       write(io,15) nx, ny
15     format(2i4)
       write(io,20) 0.0, dx*nx
       write(io,20) 0.0, dy*ny
       write(io,20) hmin, hmax
20     format(2g11.5)
c
c      now loop through the rows, printing 10 per line
c
       do 25, j=1, ny
       write(io, 30) (h(i,j), i=1,nx)
30       format(10(1X,e12.6))
25     continue
       close(io)
       return
       end
