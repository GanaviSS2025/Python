def demonstrate_boolean():
    print("=== Boolean ===")
    a, b = True, False
    print("a =", a, "| b =", b)
    print("a and b:", a and b)
    print("a or b: ", a or b)
    print("not a:   ", not a)
    print()

def demonstrate_integer():
    print("=== Integer ===")
    a, b = 10, -3
    print("a =", a, "| b =", b)
    print("a + b:", a + b)
    print("a - b:", a - b)
    print("a * b:", a * b)
    print("a / 3 :", a / 3)
    print("a // 3:", a // 3)
    print("a % 3 :", a % 3)
    print()

def demonstrate_float():
    print("=== Float ===")
    x, y = 3.14, -2.5
    print("x =", x, "| y =", y)
    print("x + y:", x + y)
    print("x - y:", x - y)
    print("x * y:", x * y)
    print("x / y:", x / y)
    print("x // y:", x // y)
    print("x % y :", x % y)
    print()

def demonstrate_string():
    print("=== String ===")
    s = "Hello, Python"
    print("s       :", s)
    print("s[1]    :", s[1])
    print("s[-1]   :", s[-1])
    print("s[0:5]  :", s[0:5])
    print("upper() :", s.upper())
    print("lower() :", s.lower())
    print("count('o'):", s.count('o'))
    print("find('Py'):", s.find('Py'))
    print("replace('Python','World'):", s.replace("Python","World"))
    print()

def demonstrate_list():
    print("=== List ===")
    lst = [1, 2, 3]
    print("lst        :", lst)
    print("lst[1]     :", lst[1])
    print("lst[-1]    :", lst[-1])
    print("lst[0:2]   :", lst[0:2])
    lst.append(4)
    print("append(4)  :", lst)
    lst.extend([5,6])
    print("extend(...) :", lst)
    lst.insert(1, 9)
    print("insert(1,9):", lst)
    print("pop(1)     :", lst.pop(1), "| now:", lst)
    lst.remove(3)
    print("remove(3)  :", lst)
    print("index(2)   :", lst.index(2))
    print("count(2)   :", lst.count(2))
    lst.sort()
    print("sort()     :", lst)
    lst.reverse()
    print("reverse()  :", lst)
    print()

def demonstrate_dict():
    print("=== Dictionary ===")
    d = {"key1":"value1","key2":"value2"}
    print("d:", d)
    print("d['key1']:", d["key1"])
    d["key3"] = "value3"
    print("after d['key3']='value3':", d)
    print("keys():", list(d.keys()))
    print("values():", list(d.values()))
    print("items():", list(d.items()))
    print("get('key2'):", d.get("key2"))
    print("pop('key1'):", d.pop("key1"), "| now:", d)
    d.update({"key4":"value4"})
    print("update(...)  :", d)
    print()

def demonstrate_tuple():
    print("=== Tuple ===")
    t = (1,2,3)
    print("t           :", t)
    print("t[1]        :", t[1])
    print("t[0:2]      :", t[0:2])
    print("len(t)      :", len(t))
    print("t + (4,5)   :", t + (4,5))
    print("t * 2       :", t * 2)
    print("count(2)    :", t.count(2))
    print("index(3)    :", t.index(3))
    print()

if __name__ == "__main__":
    demonstrate_boolean()
    demonstrate_integer()
    demonstrate_float()
    demonstrate_string()
    demonstrate_list()
    demonstrate_dict()
    demonstrate_tuple()