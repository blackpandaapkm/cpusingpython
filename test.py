if __name__ == '__main__':
    n = int(input())
    arr = []

    for i in range(n):
        element = int(input())
        arr.append(element)

    for i in range(n):
        str_element = str(arr[i])
        if str_element.startswith('7') or str_element.startswith('8') or str_element.startswith('9'):
            if len(str_element) == 10:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
