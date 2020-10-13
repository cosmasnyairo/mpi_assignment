
from numpy import trapz
from mpi4py import MPI

comm = MPI.COMM_WORLD
no_of_processes = comm.Get_size()
rank = comm.Get_rank()

# we take 3 intervals since we have 3 processes

y1 = [4, 6, 6]
y2 = [6, 4, 4]
y3 = [4, 5]

# we take the x interval value
x_interval = 2

total_area = 0

if rank != 0:
    if rank == 1:
        area = trapz(y1, dx=x_interval)
        message = area
        comm.send(message, dest=0)
    elif rank == 2:
        area = trapz(y2, dx=x_interval)
        message = area
        comm.send(message, dest=0)
    elif rank == 3:
        area = trapz(y3, dx=x_interval)
        message = area
        comm.send(message, dest=0)

else:
    for procid in range(1, no_of_processes):
        message = comm.recv(source=procid)
        total_area += message
        print('Calculated area from process {} is : {}'.format(procid, message))

if total_area>0:
    print('Total trapezium area is : {}'.format(total_area))
