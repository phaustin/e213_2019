c %G% %W%
c  *************************************************************************
c  *                                                                       *
c  *                          F l o w s s 1 d                              *
c  *                                                                       *
c  *************************************************************************
c  Programmed by: Roger Beckie
c  Last updated:  Oct. 1998
c
c  Modifications history:
c
c
c  This code solves the 1 - d steady state, heterogeneous isotropic flow 
c  equation of the form: d/dz(Kdh/dz) = 0, where h is head,
c  and K is the hydraulic conductivity.
c
c  Method
c  ======
c  This code uses a basic cell - centered finite difference formulation
c  with an SOR solver.
c
c  Inputs
c  ======
c  The code is run from a control file named flowss1d.con.
c  The control file contains some basic parameters, and the names of
c  other input and output files. See the subroutine INPUTS for information
c  on the inputs required to run the code.
c
c
c  Variables
c ===========
c h(i)  head in gridblock i, where i indexes the z direction
c (increasing downwards)
c cond(i) saturated hydraulic conductivity in gridblock i
c dz(i)  thickness of gridblock i
c n(i), c(i), s(i): n, c, s coefficient for equation in gridblock i
c
c              o N
c | z          |
c |          C |           Stencil for node  i
c |            o   
c v            |
c              |
c              o S
c
c ioecho  unit number for general echo of input.
c iohead  unit number for head output file.
c iosurf  unit number for head grid file.
c itmax, omega, tol = max iterations, accel. param. and tolerance
c  for solution.
c isflux = 1 if top gridblock is specified flux = q, 
c otherwise specified head is assumed. Bottom gridblock always
c assumed to be
c specified head.
c
       program flowss1d
       integer maxz
       parameter(maxz=2000)
       integer  nz, iohead, ioecho,  itmax, ldi, isflux
c
c      maxz is the maximum number of nodes that can be used
c      recompile program is maxz is changed
       real*8  dz(maxz), tol, omega
       real*8  cond(maxz)
       real*8  c(maxz), n(maxz)
       real*8  s(maxz), h(0:maxz)
       real*8  q, rhs(maxz)
c
c
c      set lead dimensions of arrays 
       ldi = maxz
c
c      *********************************
c      *                               *
c      *         I n p u t s           *
c      *                               *
c      *********************************
c
c
	call inputs(iohead, ioecho, isflux, nz, dz, h, q, cond,
     > itmax, omega, tol, ldi)

c
c
c      *********************************
c      *                               *
c      *   D e f i n e  c o e f f s    *
c      *                               *
c      *********************************
c
c
	call defcoefs(isflux, nz, cond, q, dz, c, n,
     >  s, h, rhs, ldi)
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
	 call sorsolver(ioecho, nz, h, c, n, s, rhs, itmax,
     >   omega, tol, ldi)
c
c      *********************************
c      *                               *
c      *         O u t p u t s         *
c      *                               *
c      *********************************
c
c
	call outputs(nz, dz, iohead, h, ldi, isflux)
c
18      end
c
c  *************************************************************************
c  *                                                                       *
c  *                             i n p u t s                               *
c  *                                                                       *
c  *************************************************************************
c  This subroutine reads in the required data and echos it out. It is
c  assummed that a file named flowss1d.con exists in the current directory
c  and contains the following (individual items separated by spaces):
c  line
c  =====
c 1: nz                 - total number of blocks in z direction
c 2: itmax, omega, tol  - maximum number of iterations, sor factor and toler.
c 3: echofile           - echo data to this file.
c 4: dzfile             - file containing dz's for grid.
c 5: headout            - head solution file name.
c 6: isflux, q          - (1 => top node is specified flux)
c                        q (ignored if sp. head)
c 7: head0file          - initial guess at heads (for const. head nodes,
c                         initial guess = bc).
c 8: logcondfile        - filename of saturated log 10 conductivity file
c
c example flowss1d.con file:
c
c  30
c  200 1.9 1.e-6
c  test.out
c  dz30.in
c  head.out
c  0 2e-5
c  h30.in
c  lk30.in
c
c
c
	 subroutine inputs(iohead, ioecho, isflux, nz, dz, h, q, cond,
     > itmax, omega, tol, ldi)
c
       integer ldi, isflux, itmax, nz, iohead, ioecho
       real*8 cond(ldi), q, h(0:ldi), omega, dz(ldi), tol
c
c      local variables
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
       open(unit = 2, file = 'flowss1d.con', status='old')
c
c      read grid parameters, then sor parameters, then echo filename.
c
       read(2, *) nz
       if(nz.gt.ldi-1) then
        print *, 'NZ too large. nz = ', nz
        print *, 'Current max size (maxz) = ', ldi - 1
        print *, 'Check inputs or recompile with larger maxz'
        stop
       endif
       read(2, *) itmax, omega, tol
       read(2, '(a)') fname
c
c      give echo file unit number 11
c
       ioecho = 11
       open(unit = ioecho, file = fname)
c
       write(ioecho, 10) nz, itmax, omega, tol, fname
10     format(//,' 1 - D finite - volume model of steady - ',
     > ' state flow', ///,
     > ' Inputs:',/,
     > ' nz: ', i3,/,
     > ' Max number of sor iterations (itmax): ', i5,/,
     > ' SOR acceleration parameter (omega): ', f5.2,/,
     > ' Solution convergence tolerance (tol): ', g8.2,/,
     > ' Name of echo file (this file): ', a)
c
c      *********************************
c      *                               *
c      *        D z    f i l e         *
c      *                               *
c      *********************************
c
c      read dz from file.
c
       io = 20
       read(2, '(a)') fname
       write(ioecho, 12) fname
12     format(' Grid spacing in filename: ', a)
       open(unit = io, file = fname)
       read(io, *) (dz(i), i=1, nz)
       close(io)
c
c      echo gridspacing to echo file
c
       write(ioecho, 17)
       write(ioecho, 18) (i, dz(i), i=1, nz)
17     format(//, ' Grid spacing:')
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
c      *          I s f l u x          *
c      *                               *
c      *********************************
c
c
       read(2, *) isflux, q
       write(ioecho, 20)  isflux, q
20     format(' Isflux (1 ==> top node is specified flux): ', i2,/,
     > ' q - specified flux into top gridblock'
     > ' (ignored for fixed head)', g12.4,/)
c
c      *********************************
c      *                               *
c      *     H e a d 0 f i l e         *
c      *                               *
c      *********************************
c      read in initial guess at head solution
c
       read(2, '(a)') fname
       write(ioecho, 30)  fname
30     format(' Initial heads filename: ', a)
       open(unit = io, file = fname)
       call readhead(io, h, nz, ldi)
c
c
c      *********************************
c      *                               *
c      *       s e t  c o n d          *
c      *                               *
c      *********************************
c
c
       io = 20
       read(2, '(a)') fname
       write(ioecho, 60) fname
60     format(' Log 10 conductivity filename: ', a,///)
       open(unit = io, file = fname)
       call setcond(io, nz, cond, ldi)
       close(io)
c
c
       return
       end
c
c  *************************************************************************
c  *                                                                       *
c  *                         r e a d h e a d                               *
c  *                                                                       *
c  *************************************************************************
c  This routine opens and reads a file containing nz real*8 and stores
c  them in an array.
c
c   io = unit number of file (opened)
c   nz = dimensions of field
c
c  *************************************************************************
       subroutine readhead(io, h, nz, ldi)
       integer io, nz, ldi
       real*8 h(0:ldi)
c
       integer i
c
c      satisfy watfor by initializing all data to zero
c
      do 10, i=0, nz + 1
	 h(i) =0.0
10    continue
       read(io, *) (h(i), i = 1, nz)
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
c  This coded determines the coefficients for the discrete approximation
c  for every node in the grid. Constant head nodes are given trivial
c  equations.
c
	 subroutine defcoefs(isflux, nz, cond, q, dz, c, n,
     >  s, h, rhs, ldi)
c
       integer nz, isflux
       real*8 condc, dz(ldi), cond(ldi)
       real*8 c(ldi), n(ldi), s(ldi)
       real*8 h(0:ldi), rhs(ldi), q
c
c      local variables
c
       integer i
       real*8 czp, czm

c
	do 10, i = 2, nz-1
c
c     set coefficients for interior nodes
c
	  czp = condc(cond(i+1), cond(i), dz(i+1), dz(i))
     >   * 2.0/(dz(i)+dz(i+1))
	  czm = condc(cond(i-1), cond(i), dz(i-1), dz(i))
     >   * 2.0/(dz(i)+dz(i-1))
	  c(i) = ((czp + czm))
	  n(i) = -czm
	  s(i) = -czp
	  rhs(i) =  0.0
10    continue
c
c     first equation
c   
      i = 1
      if(isflux.eq.1) then
c     specified flux boundary
c
	  czp = condc(cond(i+1), cond(i), dz(i+1), dz(i))
     >   * 2.0/(dz(i)+dz(i+1))
        c(i) = ((czp))
	  n(i) = 0.0
	  s(i) = -czp
	  rhs(i) = q
c      
       else
c       trivial equation for specified head
        c(i) = 1.0
        n(i) = 0.0
        s(i) = 0.0 
        rhs(i) = h(i)
       endif
c
c     last equation
c   
       i = nz
c      trivial equation for specified head
       c(i) = 1.0
       n(i) = 0.0
       s(i) = 0.0 
       rhs(i) = h(i)
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
c  *                          s e t c o n d                                *
c  *                                                                       *
c  *************************************************************************
c  This routine reads the conductivity values from a file. Every gridblock
c  must be assigned a conductivity, even if it is a constant head node.
c  
c   nz = dimensions of field
c   cond(i) conductivity in gridblock i.
c
c  *************************************************************************
       subroutine setcond(io, nz, cond, ldi)
       integer  io, nz
       real*8 cond(ldi)
c
       integer i
c
c      initialize everything to zero
c
	do 10, i=1, nz
	 cond(i) = 0.0
10    continue
c
c
       read(io,*) (cond(i), i=1,nz)
	 do 20, i=1, nz
	  cond(i) = 10**(cond(i))
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
c   z          |
c |          C |              stencil for node  i 
c |            o  
c v            |                
c              |
c              o S
c
c
c nz = size of grid
c h = current guess at head solution
c c, n, s,  rhs coefficients for equation
c itmax = on entry = max number of iterations, on exit, = number of iterations
c omega = acceleration factor
c tol = solution tolerance, ||r(k)||/ ||rhs|| < tol
c ==========================================================================
c
c
	 subroutine sorsolver(ioecho, nz, h, c, n, s, rhs, itmax,
     >   omega, tol, ldi)
       integer nz, itmax, ioecho
       real*8 h(0:ldi), c(ldi), n(ldi), s(ldi)
       real*8 omega, tol, rhs(ldi)
c
c      local variables
c
       integer i
       real*8 dh, h0, res
c
c      find h0, norm of initial residual, use in convergence criteria
c
       h0 = 0.0
	 do 10, i=1, nz
	 res =
     >         rhs(i)
     >       - n(i) * h(i-1)
     >       - s(i) * h(i+1) 
     >       - c(i) * h(i)
         h0 = h0 + (res)**2
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
	do 20, i=1, nz
	 res =
     >         rhs(i)
     >       - n(i) * h(i-1)
     >       - s(i) * h(i+1)
     >       - c(i) * h(i)
       dh = dh + (res)**2
c
c       now do relaxation step
c
	 h(i) = h(i) + omega * res/c(i)
20     continue
c
c      now check if converged
       write(ioecho, 25)  it, sqrt(dh/h0)
25     format( i6, 1x, e13.5)
c
       if(sqrt(dh/h0).lt.tol) goto 50
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
	  subroutine outputs(nz, dz, iout, h, ldi, isflux)
c
       integer nz, iout, ldi, isflux
       real*8 h(0:ldi), dz(ldi), z
        if(isflux.eq.1) then
	     z = dz(1)*0.5
	  else
	     z= 0.0
	  endif
        do 15, i=1, nz
         write(iout, 10) z, h(i)
         z = z + 0.5*(dz(i)+ dz(i+1))
10       format(g10.4, 1x, e16.9)
15     continue
       return
       end
c
