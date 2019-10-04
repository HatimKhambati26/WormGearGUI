import math


i = 0
P = int(input("Enter Power transmitted (P) in kW : "))
N1 = int(input("Enter prime mover speed (N1) in rpm: "))
choice = float(input("Select \n1.Reduction ratio(i) OR \n2.Speed of the application (N2) in rpm:\n"))
if choice == 1:
    i = float(input("\nEnter i: "))
    N2 = N1 / i
    print("\nN2=", round(N2, 2))
elif choice == 2:
    N2 = int(input("\nEnter N2: "))
    i = N1 / N2
    print("\ni=", round(i, 2))
else:
    print("Enter valid input\n")
sf = float(input("Enter value of service factor(SF): "))
Pd = P * sf
print("Design Power (Pd) is: ", Pd)
press_ang = int(input("Select pressure angle in degrees: "))
gear_qua = int(input(
    "Select gear quality \n 1. Precision gears, \n 2. Carefully cut gears \n 3. First class commercial gears \n"))
Z = int((40 / (i + 1)) + 1)
print("\nNo of starts on worm (Z)=", Z)
if Z == 1:
    eff = 0.725
if Z == 2:
    eff = 0.76
if Z == 3:
    eff = 0.86
if Z == 4:
    eff = 0.86
z = Z * i
print("\nNo of starts on worm wheel (z)=", z)
q = int(input("\nEnter the diametral quotient (q): "))
lead_ang1 = math.degrees(math.atan(Z / q))
print("\nLead angle of worm= ", round(lead_ang1, 2))
helix_ang1 = 90 - lead_ang1
print("\nHelix angle of worm= ", round(helix_ang1, 2))
helix_ang2 = lead_ang1
print("\nHelix angle of worm wheel= ", round(helix_ang2, 2))

# VIRTUAL NO OF TEETH
helix_ang1 = math.radians(helix_ang1)
helix_ang2 = math.radians(helix_ang2)
Zv1 = Z / ((math.cos(helix_ang1)) * (math.cos(helix_ang1)) * (math.cos(helix_ang1)))
Zv2 = z / ((math.cos(helix_ang2)) * (math.cos(helix_ang2)) * (math.cos(helix_ang2)))
print("\nZv1= ", round(Zv1, 2), "\nZv2= ", round(Zv2, 2))

# LEWIS FORM FACTOR
Y1 = (0.154 - (0.912 / Zv1)) * math.pi
Y2 = (0.154 - (0.912 / Zv2)) * math.pi
print("\nYv1= ", round(Y1, 2), "\nYv2= ", round(Y2, 2))

# SELECTION OF MATERIAL
worm = int(input("\nSelect the material for worm \n1.C45 \n2.15Ni2Cr1Mo25 \n3.40Ni2Cr1Mo28"))
if worm == 1:
    benstr1 = 135
    surstr1 = 500
    print("Bending stress= ", round(benstr1, 2))
    print("Surface stress= ", round(surstr1, 2))
if worm == 2:
    benstr1 = 300
    surstr1 = 950
    print("Bending stress= ", round(benstr1, 2))
    print("Surface stress= ", round(surstr1, 2))
if worm == 3:
    benstr1 = 380
    surstr1 = 1100
    print("Bending stress= ", round(benstr1, 2))
    print("Surface stress= ", round(surstr1, 2))

wheel = int(input(
    "\nSelect the material for worm wheel \n1.Chilled phosphor bronze \n2.Sand phosphor bronze \n3.Grade 25 Cast Iron "
    "\n4.Grade 35 Cast Iron"))
if wheel == 1:
    benstr2 = 110
    surstr2 = 149
    print("Bending stress= ", round(benstr2, 2))
    print("Surface stress= ", round(surstr2, 2))
if wheel == 2:
    benstr2 = 78
    surstr2 = 149
    print("Bending stress= ", round(benstr2, 2))
    print("Surface stress= ", round(surstr2, 2))
if wheel == 3:
    benstr2 = 30
    surstr2 = 149
    print("Bending stress= ", round(benstr2, 2))
    print("Surface stress= ", round(surstr2, 2))
if wheel == 4:
    benstr2 = 40
    surstr2 = 149
    print("Bending stress= ", round(benstr2, 2))
    print("Surface stress= ", round(surstr2, 2))

# SELECTION OF WEAKER ELEMENT
weak1 = benstr1 * Y1
weak2 = benstr2 * Y2
if weak1 < weak2:
    print("Since", "Strength of worm = ", round(weak1, 2), "<", "Strength of worm wheel = ", round(weak2, 2),
          "\nWorm is weaker")
else:
    print("Since", "Strength of worm wheel = ", round(weak2, 2), "<", "Strength of worm = ", round(weak1, 2),
          "\nWorm wheel is weaker")
# MODULE
if weak1 < weak2:
    Mt1 = (9.55 * 1000000 * Pd * eff) / N1
    s = (Z / q) + 1
    p = (Z / q) * surstr1 * surstr1
    a = s * (pow((540 * Mt1) / p, 0.33))
    print("\na= ", round(a, 2))
    mx = (a / (0.5 * (q + Z))) * 10
    print("\nModule= ", round(mx, 2))
    m = int(input("Enter module to be selected: "))
    # CHECK FOR BENDING
    BENSTR = (1.9 * Mt1) / (m * m * m * q * Z * Y1)
    print("\nInduced bending stress= ", round(BENSTR, 2), "< Allowable bending stress= ", benstr1)
    print("Design is safe")

    # TOOTH STRENGTH
    d = q * m
    if Z == 1:
        b = 0.75 * d
    if Z == 2 or 3:
        b = 0.75 * d
    if Z == 4:
        b = 0.67 * d
    mn = m * math.cos(helix_an1)
    Fs = benstr1 * Y2 * b * mn
    print("Fs= ", round(Fs, 2))

    # DYNAMIC LOAD
    d1 = m * Z
    Vmg = (math.pi * d1 * N1) / 60000
    Ft = (2 * Mt1) / d1
    Fd = ((6 + Vmg) / 6) * Ft
    print("Fd= ", round(Fd, 2))

    if Fs > Fd:
        print("\nFs= ", round(Fs, 2), " > Fd= ", round(Fd, 2), "\nDesign is safe")
    else:
        while Fs < Fd:
            print("\nFs= ", round(Fs, 2), " < Fd= ", round(Fd, 2), "\nDesign is not safe")
            m = int(input("Enter module to be selected: "))
            mn = m * math.cos(helix_ang1)
            Fs = benstr1 * Y1 * b * mn
            print("Fs= ", round(Fs, 2))
            d1 = m * Z
            Vmg = (math.pi * d1 * N1) / 60000
            Ft = (2 * Mt2) / d1
            Fd = ((6 + Vmg) / 6) * Ft
            print("Fd= ", round(Fd, 2))
            break
        print("\nFs= ", round(Fs, 2), " > Fd= ", round(Fd, 2), "\nDesign is safe")

    # CHECK FOR WEAR
    Dg = (m * Z) / 10
    d = q * m
    if Z == 1:
        b = 0.75 * d
    if Z == 2 or 3:
        b = 0.75 * d
    if Z == 4:
        b = 0.67 * d
    b = b / 10
    Kw = float(input("\nEnter the value of wear factor: "))
    Fw = Dg * b * Kw * 10
    print("\nFw= ", round(Fw, 2))
    if Fw > Fd:
        print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
    else:
        while Fw < Fd:
            print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is not safe")
            m = int(input("Enter module to be selected: "))
            Dg = (m * Z) / 10
            d = q * m
            if Z == 1:
                b = 0.75 * d
            if Z == 2 or 3:
                b = 0.75 * d
            if Z == 4:
                b = 0.67 * d
            b = b / 10
            Kw = float(input("\nEnter the value of wear factor: "))
            Fw = Dg * b * Kw * 10
            break
        print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")

if weak2 < weak1:
    Mt2 = (9.55 * 1000000 * Pd * eff) / N2
    s = (z / q) + 1
    p = (z / q) * surstr2 * 10 * surstr2 * 10
    a = s * (pow((540 * Mt2) / p, 0.33))
    print("\na= ", round(a, 2))
    mx = (a / (0.5 * (q + z))) * 10
    print("\nModule= ", round(mx, 2))
    m = int(input("Enter module to be selected: "))

    # CHECK FOR BENDING
    BENSTR = (1.9 * Mt2) / (m * m * m * q * z * Y2)
    print("\nInduced bending stress= ", round(BENSTR, 2), "< Allowable bending stress= ", benstr2)
    print("\nDesign is safe")

    # TOOTH STRENGTH
    d = q * m
    if Z == 1:
        b = 0.75 * d
    if Z == 2 or 3:
        b = 0.75 * d
    if Z == 4:
        b = 0.67 * d
    mn = m * math.cos(helix_ang2)
    Fs = benstr2 * Y2 * b * mn
    print("Fs= ", round(Fs, 2))

    # DYNAMIC LOAD
    d2 = m * z
    Vmg = (math.pi * d * N2) / 60000
    Ft = (2 * Mt2) / d2
    Fd = ((6 + Vmg) / 6) * Ft
    print("Fd= ", round(Fd, 2))

    if Fs > Fd:
        print("\nFs= ", round(Fs, 2), " > Fd= ", round(Fd, 2), "\nDesign is safe")
    else:
        while Fs < Fd:
            print("\nFs= ", round(Fs, 2), " < Fd= ", round(Fd, 2,), "\nDesign is not safe")
            m = int(input("Enter module to be selected: "))
            mn = m * math.cos(helix_ang2)
            Fs = benstr2 * Y2 * b * mn
            print("Fs= ", round(Fs, 2))
            d2 = m * z
            Vmg = (math.pi * d * N2) / 60000
            Ft = (2 * Mt2) / d2
            Fd = ((6 + Vmg) / 6) * Ft
            print("Fd= ", round(Fd, 2))
            break
        print("\nFs= ", round(Fs, 2), " > Fd= ", round(Fd, 2), "\nDesign is safe")

    # CHECK FOR WEAR
    Dg = (m * z) / 10
    d = q * m
    if Z == 1:
        b = 0.75 * d
    if Z == 2 or 3:
        b = 0.75 * d
    if Z == 4:
        b = 0.67 * d
    b = b / 10
    Kw = float(input("\nEnter the value of wear factor: "))
    Fw = Dg * b * Kw * 10
    print("\nFw= ", round(Fw, 2))
    if Fw > Fd:
        print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
    else:
        while Fw < Fd:
            print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is not safe")
            m = int(input("Enter module to be selected: "))
            Dg = (m * z) / 10
            d = q * m
            if Z == 1:
                b = 0.75 * d
            if Z == 2 or 3:
                b = 0.75 * d
            if Z == 4:
                b = 0.67 * d
            b = b / 10
            Kw = float(input("\nEnter the value of wear factor: "))
            Fw = Dg * b * Kw * 10
            break
        print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")

# THERMAL CHECK
Hg = Pd * (1 - eff)
print("\nHg=", round(Hg, 2))
h = float(input("Enter the value of h: "))
Ta = float(input("Enter Ta in Kelvin: "))
T = float(input("Enter T in Kelvin: "))
sigma = float(input("Enter the value of sigma: "))
Hd = h * (T - Ta) + (sigma / 100000000) * (pow(T, 4) - pow(Ta, 4))
print("Hd=", round(Hd, 2))
A = (Hg * 1000) / Hd
print("A=", round(A, 2))
d1 = m * q
d2 = m * z
a = (d1 + d2) / 2
a = a / 10
AA = 57.2 * pow(a, 1.7)
AA = AA / 10000
if AA > A:
    print("[A]= ", round(AA, 2), "> A= ", round(A, 2), "\nDesign is safe")
else:
    while AA < A:
        print("[A]= ", round(AA, 2), "< A= ", round(A, 2), "\nDesign is not safe")
        h = float(input("Enter the value of h: "))
        Hd = h * (T - Ta) + (sigma / 100000000) * (pow(T, 4) - pow(Ta, 4))
        print("Hd=", round(Hd, 2))
        A = (Hg * 1000) / Hd
    print("[A]= ", round(AA, 2), "> A= ", round(A, 2), "\nDesign is safe")
