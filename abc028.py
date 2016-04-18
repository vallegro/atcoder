N, k = [int(i) for i in input().split()]
if k > N:
    print(str(0))
else:
    c = (2*k-1)*(N-k)+k*(N-k)+N+(N-k+1)*(k-1)+(2*(N-k)+1)*(k-1)
    print(str(c/(N*N*N)))
