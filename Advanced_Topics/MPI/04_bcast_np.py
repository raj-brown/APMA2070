from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N=100  # Size of Buffer

if rank == 0:
    data = np.arange(N, dtype='i')
else:
    data = np.empty(N, dtype='i')

comm.Bcast(data, root=0)

for i in range(0, N):
    assert data[i] == i

