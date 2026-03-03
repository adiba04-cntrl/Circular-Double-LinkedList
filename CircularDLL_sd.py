import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

class CircularDLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return

        tail = self.head.prev
        tail.next = new
        new.prev = tail
        new.next = self.head
        self.head.prev = new

    def size(self):
        if not self.head:
            return 0
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

    def delete(self, pos):
        n = self.size()
        if pos < 1 or pos > n:
            print("Nomor tidak valid!")
            return

        temp = self.head
        if pos == 1:
            if n == 1:
                self.head = None
                return
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head
            return

        for _ in range(1, pos):
            temp = temp.next

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def forward(self):
        if not self.head:
            print("Tidak ada berita.")
            return

        temp = self.head
        no = 1
        while True:
            print(f"{no}. {temp.data}")
            time.sleep(3)
            temp = temp.next
            no += 1
            if temp == self.head:
                break

    def backward(self):
        if not self.head:
            print("Tidak ada berita.")
            return

        temp = self.head.prev
        last = temp
        no = self.size()
        while True:
            print(f"{no}. {temp.data}")
            time.sleep(3)
            temp = temp.prev
            no -= 1
            if temp == last:
                break

    def show_at(self, pos):
        n = self.size()
        if pos < 1 or pos > n:
            print("Nomor tidak valid!")
            return

        temp = self.head
        for _ in range(1, pos):
            temp = temp.next

        print(f"{pos}. {temp.data}")


# MAIN
cdll = CircularDLL()

while True:
    print("\nMENU")
    print("1. Insert berita")
    print("2. Hapus berita")
    print("3. Tampilkan forward")
    print("4. Tampilkan backward")
    print("5. Tampil berita tertentu")
    print("6. Exit")

    pilih = int(input("Pilih: "))

    if pilih == 1:
        cdll.insert(input("Masukkan berita: "))

    elif pilih == 2:
        print(f"Nomor berita (1-{cdll.size()}): ", end="")
        cdll.delete(int(input()))

    elif pilih == 3:
        cdll.forward()

    elif pilih == 4:
        cdll.backward()

    elif pilih == 5:
        print(f"Nomor berita (1-{cdll.size()}): ", end="")
        cdll.show_at(int(input()))

    elif pilih == 6:
        break