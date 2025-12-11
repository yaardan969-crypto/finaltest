# 2. Contoh Algoritma Stack
# a. Single Stack
# Implementasi stack sederhana menggunakan list.
print("--- Single Stack ---")
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)
        print(f"Push: {item}, Stack: {self.items}")

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Pop: {item}, Stack: {self.items}")
            return item
        print("Stack is empty.")
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

# Penggunaan Single Stack
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.pop()
s.pop()
s.pop() # Mencoba pop dari stack kosong
print("-" * 25)


# b. Double Stack
# Mengelola dua stack dalam satu list untuk efisiensi memori.
print("--- Double Stack ---")
class DoubleStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top1 = -1  # Tumbuh dari kiri ke kanan
        self.top2 = self.capacity  # Tumbuh dari kanan ke kiri

    # --- Operasi untuk Stack 1 ---
    def push1(self, item):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.items[self.top1] = item
            print(f"Push1: {item}, Array: {self.items}")
        else:
            print("Stack 1 Overflow")

    def pop1(self):
        if self.top1 >= 0:
            item = self.items[self.top1]
            self.items[self.top1] = None
            self.top1 -= 1
            print(f"Pop1: {item}, Array: {self.items}")
            return item
        else:
            print("Stack 1 Underflow")
            return None

    # --- Operasi untuk Stack 2 ---
    def push2(self, item):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.items[self.top2] = item
            print(f"Push2: {item}, Array: {self.items}")
        else:
            print("Stack 2 Overflow")

    def pop2(self):
        if self.top2 < self.capacity:
            item = self.items[self.top2]
            self.items[self.top2] = None
            self.top2 += 1
            print(f"Pop2: {item}, Array: {self.items}")
            return item
        else:
            print("Stack 2 Underflow")
            return None

# Penggunaan Double Stack
ds = DoubleStack(5)
ds.push1(1)
ds.push2(10)
ds.push1(2)
ds.push2(9)
ds.push1(3)
ds.push1(4) # Akan overflow
ds.pop1()
ds.pop2()
print("-" * 25)
