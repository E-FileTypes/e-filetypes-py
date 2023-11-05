from timeit import timeit
from e_filetypes_py import efiletypes

"""
10MB file
"""
def testEncrypt10MBWithChunking():
    '''
    Encrypts a 10MB file using chunking.
    '''
    data = b'\x00' * (10485760)  # 10MB of null bytes
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 10MB 10 times file with chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'})",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    print(f"Time taken: {time} seconds")
def testEncrypt10MBNoChunking():
    '''
    Encrypts a 10MB file using chunking.
    '''
    data = b'\x00' * (10485760)  # 10MB of null bytes
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 10MB file 10 times without chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'}, chunking=False)",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    efiletypes.encrypt
    print(f"Time taken: {time} seconds")
"""
100MB file
"""
def testEncrypt100MBWithChunking():
    '''
    Encrypts a 100MB file using chunking.
    '''
    data = b'\x00' * (104857600)
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 100MB 10 times file with chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'})",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    print(f"Time taken: {time} seconds")
def testEncrypt100MBNoChunking():
    '''
    Encrypts a 100MB file using chunking.
    '''
    data = b'\x00' * (104857600) 
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 100MB file 10 times without chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'}, chunking=False)",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    efiletypes.encrypt
    print(f"Time taken: {time} seconds")
"""
1GB file
"""
def testEncrypt1GBWithChunking():
    '''
    Encrypts a 1GB file using chunking.
    '''
    data = b'\x00' * (1073741824)
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 1GB 10 times file with chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'})",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    print(f"Time taken: {time} seconds")
def testEncrypt1GBNoChunking():
    '''
    Encrypts a 1GB file using chunking.
    '''
    data = b'\x00' * (1073741824) 
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 1GB file 10 times without chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'}, chunking=False)",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    efiletypes.encrypt
    print(f"Time taken: {time} seconds")
"""
10GB file
"""
def testEncrypt10GBWithChunking():
    '''
    Encrypts a 10GB file using chunking.
    '''
    data = b'\x00' * (10737418240)
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 10GB 10 times file with chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'})",
        "from e_filetypes_py import efiletypes",
        number=10
    )
    print(f"Time taken: {time} seconds")
def testEncrypt10GBNoChunking():
    '''
    Encrypts a 10GB file using chunking.
    '''
    data = b'\x00' * (10737418240) 
    with open('test.txt', 'wb+') as f:
        f.write(data)
    print("Encrypting 10GB file 10 times without chunking...")
    time = timeit(
        "efiletypes.encrypt('test.txt', 'benchmark', {'test': 'test'}, chunking=False)",
        "from e_filetypes_py import efiletypes",
        number=1
    )
    efiletypes.encrypt
    print(f"Time taken: {time} seconds")

testEncrypt10MBWithChunking()
testEncrypt10MBNoChunking()
testEncrypt100MBWithChunking()
testEncrypt100MBNoChunking()
testEncrypt1GBWithChunking()
testEncrypt1GBNoChunking()
testEncrypt10GBWithChunking()
testEncrypt10GBNoChunking()