c
c  *************************************************************************
c  *                                                                       *
c  *                            f l u x i t                                *
c  *                                                                       *
c  *************************************************************************
c  This routine computes the flux through all four faces of constant head 
c  nodes. This information can be used to check water balances etc. 
c  CONVENTION: flux out of constant-head node is negative, flux in is positive.
c
      SUBROUTINE fluxit(nx, ny, dx, dy, ind, h, T, io, ldi, ldj)
C
       integer nx, ny, io, ldi, ldj, ind(ldi, *)
       real*8 dx(0:ldi), dy(0:ldj), h(0:ldi+1,0:*)
       real*8 condc, t(0:ldi+1, 0:ldj+1),  qw, qs, qn, qe, qin, qout
c        
c
c
       qin=0.0
       qout=0.0
       write(io, 5)
5      format(//,'Flux through constant-head nodes',//,
     > '   i  j       qw            qe             qs          qn'
     > ,/, '-------------------------------------------------',
     > '--------------')
       do 10, j=1, ny
       do 10, i=1, nx
         if(ind(i,j).eq.1) then
           if(ind(i-1,j).eq.0) then
             qw = dy(j) * condc(t(i-1,j), t(i,j), dx(i-1), dx(i))
     >           * (h(i-1,j) - h(i,j)) / (0.5*(dx(i-1) + dx(i)))
           else
             qw =0.0
           endif
           if(ind(i+1,j).eq.0) then
             qe = dy(j) * condc(t(i+1,j), t(i,j), dx(i+1), dx(i)) 
     >           * (h(i+1,j) - h(i,j)) / (0.5*(dx(i+1) + dx(i)))
           else
             qe =0.0
           endif
           if(ind(i,j-1).eq.0) then
             qs = dx(i) * condc(t(i,j-1), t(i,j), dy(j-1), dy(j))
     >             * (h(i,j-1) - h(i,j))/(0.5*(dy(j-1) + dy(j)))
           else
             qs =0.0
           endif
           if(ind(i,j+1).eq.0) then
             qn = dx(i) * condc(t(i,j+1), t(i,j), dy(j+1), dy(j))
     >                * (h(i,j+1) - h(i,j))/(0.5*(dy(j+1) + dy(j)))
           else
             qn =0.0
           endif
           write(io,20) i, j, qw, qe, qs, qn
20         format(i3,1x,i3, 3x, 4(e12.5, 1x))
           if(qw.gt.0.0) then
               qin=qin+qw
           else
               qout=qout+qw
           endif
           if(qe.gt.0.0) then
               qin=qin+qe
           else
               qout=qout+qe
           endif
           if(qs.gt.0.0) then
               qin=qin+qs
           else
               qout=qout+qs
           endif
           if(qn.gt.0.0) then
               qin=qin+qn
           else
               qout=qout+qn
           endif
          endif
10    continue
      write(io, 30) qin, qout, ((qin+qout)/qout)*100.
30    format(//,'Total flow through constant head cells:',/,
     > 'Q in :',e12.5,/,'Q out:',e12.5,/,'Diff: ',e12.5,' %',//,
     > 'Does not include water lost or gained through pumping and',
     > ' recharge.')
      end
           
