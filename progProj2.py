class Matrices:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    def display(self,C):
        print('Resultant Matrix is:')
        for i in range(0,m):
            print('\n')
            for j in range(0,n):
                print(' {}'.format(C[i][j]),end=" ")
    def Add(self,C):
        for i in range(0,m):
            for j in range(0,n):
                C[i][j] = A[i][j] + B[i][j]
    def Sub(self,C):
        for i in range(0,m):
            for j in range(0,n):
                C[i][j] = A[i][j] - B[i][j]
    def Mul(self,C):
        for i in range(0,m):
            for j in range(0,q):
                for k in range(0,n):
                    C[i][j]+= A[i][k] * B[k][j]
if __name__=='__main__':
    m = int(input('Enter no. of rows for Matrix 1:'))
    n = int(input('Enter no. of columns for Matrix 1:'))
    A = [[0 for j in range(0, n)] for i in range(0, m)]
    print('Enter Elements of Matrix A')
    for i in range(0, m):
        for j in range(0, n):
            A[i][j] = int(input('Enter element A{}{}:'.format(i, j)))
    p = int(input('Enter no. of rows for Matrix 2:'))
    q = int(input('Enter no. of columns for Matrix 2:'))
    B = [[0 for j in range(0, q)] for i in range(0, p)]
    print('Enter Elements of Matrix B')
    for i in range(0, p):
        for j in range(0, q):
            B[i][j] = int(input('Enter element B{}{}:'.format(i, j)))
    obj = Matrices(A,B)
    var =1
    while var!='0':
        print('1.Add Matrices\n2.Subtract Matrices\n3.Multiply Matrices\n4.Exit')
        choice = int(input('Enter Choice:'))
        if choice==1:
            if m==p and n==q:
                print('Matrices can be Added')
                C = [[0 for j in range(0, n)] for i in range(0, m)]
                obj.Add(C)
                obj.display(C)
            else:
                print('Matrices cannot be Added')
        elif choice==2:
            if m==p and n==q:
                print('Matrices can be Subtracted')
                C = [[0 for j in range(0, n)] for i in range(0, m)]
                obj.Sub(C)
                obj.display(C)
            else:
                print('Matrices cannot be Subtracted')
        elif choice==3:
            if n==p:
                print('Matrices can be Multiplied')
                C = [[0 for j in range(0, q)] for i in range(0, m)]
                obj.Mul(C)
                obj.display(C)
            else:
                print('Matrices cannot be Multiplied')
        elif choice==4:
            exit(0)
        else:
            print('\nPlease enter a valid choice')
        var = (input('\nDo you want to Continue?(press 0 to stop)'))