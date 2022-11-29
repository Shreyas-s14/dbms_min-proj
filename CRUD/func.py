#primes
p = 11111
m = 10**9+9

def cname_hash(cname):
    sum = 0
    for i,chr in enumerate(cname):
        sum += (ord(chr)*(p**i))%m
    return sum

if __name__ == "__main__":
    print(cname_hash("kkk1"))
