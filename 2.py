# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для
# всех значений предикат.
x = [False, False, False, False, True, True, True, True]
y = [False, False, True, True, False, False, True, True]
z = [False, True, False, True, False, True, False, True]

for i in range(len(x)):
    print(not(x[i] or y[i] or z[i]) == (not x[i] and not y[i] and not z[i]))