import time
t0 = time.time()
while time.time() - t0 < 10:
    time.sleep(2)
    print("whileLoop")
