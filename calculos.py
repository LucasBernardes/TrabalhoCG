def vetorNormal(P1, P2, P3):
    print(P1, P2, P3)
    nx = ((P3[1]-P1[1])*(P2[2]-P1[2])) - ((P3[2]-P1[2])*(P2[1]-P1[1]))
    ny = ((P3[2]-P1[2])*(P2[0]-P1[0])) - ((P3[0]-P1[0])*(P2[2]-P1[2]))
    nz = ((P3[0]-P1[0])*(P2[1]-P1[1])) - ((P3[1]-P1[1])*(P2[0]-P1[0]))

    print(nx,ny,nz)
    return [nx, ny, nz]

def calculoD(N, P, C):
    d0 = P[0]*N[0] + P[1]*N[1] + P[2]*N[2]
    d1 = C[0]*N[0] + C[1]*N[1] + C[2]*N[2]
    d  = d0 - d1

    return (d0, d1, d)

def matPersp(N, C, d, d0):
    M = [[0.0 for i in range(4)] for j in range(4)]
    
    M[0][0] = d + C[0] * N[0]
    M[0][1] = C[0] * N[0]
    M[0][2] = C[0] * N[2]
    M[0][3] = -C[0]*d0
    
    M[1][0] = C[1] * N[0]
    M[1][1] = d + C[1] * N[1]
    M[1][2] = C[1] * N[2]
    M[1][3] = -C[1] * d0
    
    M[2][0] = C[2] * N[0]
    M[2][1] = C[2] * N[1]
    M[2][2] = d + C[2] * N[2]
    M[2][3] = -C[2] * d0
    
    M[3][0] = N[0]
    M[3][1] = N[1]
    M[3][2] = N[2]
    M[3][3] = 1

    return M

def matPar(N, C, d0, d1):
    M = [[0.0 for i in range(4)] for j in range(4)]

    M[0][0] = d1 + C[0] * N[0]
    M[0][1] = -C[0] * N[1]
    M[0][2] = -C[0] * N[2]
    M[0][3] = C[0] * d0

    M[1][0] = -C[1] * N[0]
    M[1][1] = d1 - C[1] * N[1]
    M[1][2] = -C[1] * N[2]
    M[1][3] = C[1] * d0

    M[2][0] = -C[2] * N[0]
    M[2][1] = -C[2] * N[0]
    M[2][2] = d1 - C[2] * N[2]
    M[2][3] = C[2] * d0

    M[3][0] = 0
    M[3][1] = 0
    M[3][2] = 0
    M[3][3] = d1

    return M

def cartesiano(M):
    size = len(M)
    Mc[size][size]

    for i in range(size):
        for j in range(size):
            Mc[i][j] = M[i][j]/M[3][j]

    return Mc

def mMatrizes(A, B):
    size = len(A)
    sizeb = len(B[0])
    M = [[0.0 for i in range(sizeb)] for j in range(size)]
    
    for i in range(size):
        for j in range(sizeb):
            soma = 0.0
            for k in range(size):
                soma += A[i][k] * B[k][j]

            M[i][j] = soma
    return M
