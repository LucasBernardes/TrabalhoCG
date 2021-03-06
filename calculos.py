import math

def vetorNormal(P1, P2, P3):
    a1 = P1[0] - P2[0]
    a2 = P1[1] - P2[1]
    a3 = P1[2] - P2[2]
    b1 = P3[0] - P2[0]
    b2 = P3[1] - P2[1]
    b3 = P3[2] - P2[2]

    i = a2*b3 - a3*b2
    j = a3*b1 - a1*b3
    k = a1*b2 - a2*b1
    s = math.sqrt((i * i) + (j * j) + (k * k))

    return [i/s, j/s, k/s]

def calculoD(N, P, C):
    d0 = P[0]*N[0] + P[1]*N[1] + P[2]*N[2]
    d1 = C[0]*N[0] + C[1]*N[1] + C[2]*N[2]
    d  = d0 - d1

    return (d0, d1, d)

def matPersp(N, C, d, d0, d1):
    M = [[0.0 for i in range(4)] for j in range(4)]
    
    M[0][0] = d + C[0] * N[0]
    M[0][1] = C[0] * N[1]
    M[0][2] = C[0] * N[2]
    M[0][3] = -C[0] * d0
    
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
    M[3][3] = -d1

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

def minMax(M):
    xmin = M[0][0]
    xmax = M[0][0]
    ymin = M[1][0]
    ymax = M[1][0]
                        
    for i in range(1, len(M[0])):
        if xmin > M[0][i]:
            xmin = M[0][i]
        if xmax < M[0][i]:
            xmax = M[0][i]
        if ymin > M[1][i]:
            ymin = M[1][i]
        if ymax < M[1][i]:
            ymax = M[1][i]

    return xmin, xmax, ymin, ymax

def matED(xy, uv, M):    
    sx = (uv[1] - uv[0])/(xy[1] - xy[0])
    sy = (uv[3] - uv[2])/(xy[3] - xy[2])

    matED = [[0 for i in range(4)] for j in range(4)]

    matED[0][0] = sx
    matED[0][2] = sx*xy[0]
    matED[1][1] = -sy
    matED[1][2] = -sy*xy[2]
    matED[2][2] = 1
    matED[3][3] = 1
    
    return mMatrizes(matED, M)

def coordenadas(M):
    R = [[0 for i in range(len(M[0]))] for j in range(3)]

    for i in range(3):
        for j in range(len(M[0])):
            if (i == 0 or i == 1):
                if M[3][j] != 0:
                    R[i][j] = M[i][j]/M[3][j]
                else:
                    R[i][j] = M[i][j]
            if (i == 2):
                R[i][j] = 1

    return R
