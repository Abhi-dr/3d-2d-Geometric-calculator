line = "_" * 75

def l():
    l=float(input("Enter the value of Length:- "))
    return l

def b():
    b = float(input("Enter the value of Breadth:- "))
    return b

def h():
    h = float(input("Enter the value of Height:- "))
    return h

def r():
    r = float(input("Enter the value of Radius:- "))
    return r

def a():
    a = float(input("Enter the value of Side:- "))
    return a

def big_r():
    big_r = float(input("Enter the value of Bigger Radius:- "))
    return big_r

class Three_D:
    class Cube:

        def volume(a):
            print(f"The volume is = {a ** 3} cubic unit \n{line}")

        def csa(a):
            print(f"The C.S.A is = {4 * a ** 2} sq.unit \n{line}")

        def tsa(a):
            print(f"The T.S.A is = {6 * a ** 2} sq. unit \n{line}")

        def diagonal(a):
            print(f"The diagonal is = {a * 3 ** 0.5} unit \n{line}")

    class Cuboid:

        def volume(l, b, h):
            print(f"The volume is = {l * b * h} cubic unit \n{line}")

        def csa(l, b, h):
            print(f"The C.S.A is = {2 * (l + b) * h} sq. unit \n{line}")

        def tsa(l, b, h):
            print(f"The T.S.A is = {2 * (l * b + b * h + h * l)} sq. unit \n{line}")

        def diagonal(l, b, h):
            print(f"The diagonal is = {(l ** 2 + b ** 2 + h ** 2) ** 0.5} unit \n{line}")

    class Cylinder:

        def volume(r, h):
            print(f"The volume is = {(22/7) * r ** 2 * h} cubic unit \n{line}")

        def csa(r, h):
            print(f"The C.S.A is = {2 * (22/7) * r * h} sq. unit \n{line}")

        def tsa(r, h):
            print(f"The T.S.A is = {2 * (22/7) * r * (h + r)} sq. unit \n{line}")

    class Cone:

        def volume(r, h):
            print(f"The volume is = {(1 / 3) * (22/7) * r ** 2 * h} cubic unit \n{line}")

        def csa(r, l):
            print(f"The C.S.A is = {(22/7) * r * l} sq. unit \n{line}")

        def tsa(r, l):
            print(f"The T.S.A is = {(22/7) * r * (l + r)} sq. unit \n{line}")

        def slant_height(r, h):
            print(f"The Slant Height is = {(r * r + h * h) ** 0.5} unit \n{line}")

    class Sphere:

        def volume(r):
            print(f"The volume is = {(4 / 3) * (22/7) * r ** 3} cubic unit \n{line}")

        def csa(r):
            print(f"The C.S.A is = {4 * (22/7) * r ** 2} sq.unit \n{line}")

        def tsa(r):
            print(f"The T.S.A is = {4 * (22/7) * r ** 2} sq. unit \n{line}")

    class Hemi_Sphere:

        def volume(r):
            print(f"The volume is = {(2 / 3) * (22/7) * r ** 3} cubic unit \n{line}")

        def csa(r):
            print(f"The C.S.A is = {2 * (22/7) * r ** 3} sq.unit \n{line}")

        def tsa(r):
            print(f"The T.S.A is = {3 * (22/7) * r ** 3} sq. unit \n{line}")

    class Frustum:

        def volume(r, big_r, h):
            print(f"The volume is = ~{(1 / 3) * (22/7) * h * (big_r ** 2 + r ** 2 + big_r * r)} cubic unit \n{line}")

        def csa(r, big_r, l):
            print(f"The C.S.A is = {(22/7) * l * (big_r + r)} sq.unit \n{line}")

        def tsa(r, big_r, l):
            print(f"The T.S.A is = {(22/7) * (big_r ** 2 + r ** 2 + l * (big_r + r))} sq. unit \n{line}")

        def slant_height(r, big_r, h):
            print(f"The Slatn Height is = {(h * h + (big_r - r) ** 2) ** 0.5} unit \n{line}")


try:
    while True:
        print("1. Cube\n2. Cuboid\n3. Cylinder\n4. Cone\n5. Sphere\n6. Hemi Sphere\n7. Frustum")
        n = int(input("Enter your choice:- "))

        if n == 1:  #Cube
            q = int(input("What do you want to find in Cube?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Diagonal\n>>> "))
            if q == 1:
                Three_D.Cube.volume(a())

            elif q == 2:
                Three_D.Cube.csa(a())

            elif q == 3:
                Three_D.Cube.tsa(a())

            elif q == 4:
                Three_D.Cube.diagonal(a())

            else:
                print("Something is wrong... Try Again!!")
                continue

        elif n == 2: #cuboid
            q = int(input("What do you want to find in Cuboid?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Diagonal\n>>> "))

            if q == 1:
                Three_D.Cuboid.volume(l(), b(), h())

            elif q == 2:
                Three_D.Cuboid.csa(l(), b(), h())

            elif q == 3:
                Three_D.Cuboid.tsa(l(), b(), h())

            elif q == 4:
                Three_D.Cuboid.diagonal(l(), b(), h())

            else:
                print("Something is wrong... Try Again!!")
                continue

        elif n==3: #cylinder
            q=int(input("What do you want to find in Cylinder?... \n1. Volume\n2. C.S.A\n3. T.S.A\n>>> "))
            if q==1:
                Three_D.Cylinder.volume(r(), h())

            elif q==2:
                Three_D.Cylinder.csa(r(), h())

            elif q==3:
                Three_D.Cylinder.tsa(r(), h())

            else:
                print("Something is wrong... Try Again!!")
                continue

        elif n==4: #cone
            q = int(input("What do you want to find in Cone?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Slant Height\n>>> "))
            if q==1:
                Three_D.Cone.volume(r(), h())

            elif q==2:
                Three_D.Cone.csa(r(), l())

            elif q==3:
                Three_D.Cone.tsa(r(), l())

            elif q==4:
                Three_D.Cone.slant_height(r(), h())

            else:
                print("Something is wrong... Try Again!!!")
                continue

        elif n==5: #sphere
            q = int(input("What do you want to find in Sphere?... \n1. Volume\n2. C.S.A\n3. T.S.A\n>>> "))
            if q == 1:
                Three_D.Sphere.volume(r())

            elif q == 2:
                Three_D.Sphere.csa(r())

            elif q == 3:
                Three_D.Sphere.tsa(r())

            else:
                print("Something is wrong... Try Again!!")
                continue

        elif n==6: #hemi-sphere
            q = int(input("What do you want to find in Hemi-Sphere?... \n1. Volume\n2. C.S.A\n3. T.S.A\n>>> "))
            if q == 1:
                Three_D.Hemi_Sphere.volume(r())

            elif q == 2:
                Three_D.Hemi_Sphere.csa(r())

            elif q == 3:
                Three_D.Hemi_Sphere.tsa(r())

            else:
                print("Something is wrong... Try Again!!")
                continue

        elif n==7:
            q = int(
                input("What do you want to find in Frustum?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Slant Height\n>>> "))
            if q == 1:
                Three_D.Frustum.volume(r(), big_r(), h())

            elif q == 2:
                Three_D.Frustum.csa(r(), big_r(), l())

            elif q == 3:
                Three_D.Frustum.tsa(r(), big_r(), l())

            elif q == 4:
                Three_D.Frustum.slant_height(r(), big_r(), h())

            else:
                print("Something is wrong... Try Again!!!")
                continue

        else:
            print("Invalid!!... Try Again!!")
            continue

except:
    print("Invalid!!!")