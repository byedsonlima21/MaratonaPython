
def verificador(*num):
    lst = []
    for n in range(0, len(num)):
        lst.append(num[n])
    maior = max(lst)
    print(f"A lista passada foi: {lst}")
    print(f"O maior valor da lista é: {maior}")

verificador(1, 5, 7)
print()
verificador(8, 6, 9, 0)
