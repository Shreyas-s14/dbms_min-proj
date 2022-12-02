#primes
p = 31
m = 11111

def cname_hash(cname):
    sum = 0
    for i,chr in enumerate(cname):
        sum += (ord(chr)*(p**i))%m
    return sum

def reverse_cname_hash(hash):
    cname = ""
    while hash != 0:
        cname = chr(hash%p) + cname
        hash //= p
    return cname
if __name__ == "__main__":
    print(cname_hash("kkk1"))
    print(reverse_cname_hash(23450))
