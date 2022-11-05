def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def n_length_combo(lst, n):

    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):
        # หยิบตัวที่น้อยที่สุดออกก่อน
        m = lst[i]
        remLst = lst[i + 1:]
        # ส่งตัวที่เหลือไปหา combo
        remainlst_combo = n_length_combo(remLst, n-1)
        # นำตัวที่น้อยที่สุดเอามารวมกับ combo ที่ได้หามา
        for p in remainlst_combo:
            l.append([m, *p])

    return l


def findcomb(lst):
    ans = []
    for i in range(1, len(lst)+1):
        ans = ans + n_length_combo(lst, i)
    return ans


def findlist(num, lst):
    ans = []
    for i in lst:
        if num == sum(i):
            ans.append(insertionSort(i))
    return ans


num, lst = input("Enter Input : ").split('/')
lst = list(map(int, lst.split(' ')))
lst = insertionSort(lst)
lst = findcomb(lst)
lst = findlist(int(num), lst)
if lst == []:
    print("No Subset")
    exit()
print(*lst, sep='\n')
