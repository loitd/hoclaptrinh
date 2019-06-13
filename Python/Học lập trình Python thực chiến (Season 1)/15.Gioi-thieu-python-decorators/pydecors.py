# -------------------------------------------------------
# Bài 15: Giới thiệu về Python Decorator
# Kênh youtube: youtube.com/c/tranducloi
# -------------------------------------------------------
import time

# Khai bao timer decorator
def timedecor(func):
    # Khai bao timer decorator wrapper
    def wrapper(*args, **kwargs):
        t1 = time.time()
        # Thuc hien ham func() -> Da them cac tham so trong loi goi ham thong qua ham wrapper
        func(*args, **kwargs)
        t2 = time.time()
        print("Da chay xong trong: {0}s".format(t2-t1))
        # Them phan return function de ho tro nhung ham co gia tri tra ve
        return func(*args, **kwargs)
    return wrapper

@timedecor
def dummy(name):
    print("dang chay ham dummy {0}".format(name))
    time.sleep(3)
    return 3.14

# Cach 3: # Loi goi ham
print(dummy("Loitd"))

# def dummy2():
#     print("dang chay ham dummy2")
#     time.sleep(3)

# def dummy3():
#     print("dang chay ham dummy3")
#     time.sleep(3)
# Cach 1
# timedecor(dummy2)()
# timedecor(dummy3)()

# Cach 2
# timedecor_call = timedecor(dummy2)
# timedecor_call()
# timedecor_call = timedecor(dummy3)
# timedecor_call()




