class HashTable:
    def init(self, size=2, load_factor=0.75, p=7):
        self._size = size
        self._load_factor = load_factor
        self._p = p
        self._count = 0
        self._table = [[] for _ in range(size)]

    # ---------- ХЕШ-ФУНКЦІЯ ----------
    def _hash(self, key):
        if isinstance(key, int):
            v = key
            return v % self._size

        if isinstance(key, float):
            v = int(key * 1000)
            return v % self._size

        # string or others
        h = 0
        for ch in str(key):
            h = (h * self._p + ord(ch)) % self._size
        return h

    # ---------- RESIZE ----------
    def _resize(self):
        old_table = self._table
        self._size *= 2
        self._table = [[] for _ in range(self._size)]
        self._count = 0

        for bucket in old_table:
            for key, value in bucket:
                self[key] = value

    # ---------- SETITEM ----------
    def setitem(self, key, value):
        if self._count / self._size >= self._load_factor:
            self._resize()

        index = self._hash(key)
        bucket = self._table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._count += 1

    # ---------- GETITEM ----------
    def getitem(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key {key} not found")

    # ---------- LEN ----------
    def len(self):
        return self._count

    # ---------- POP ----------
    def pop(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                self._count -= 1
                return bucket.pop(i)[1]

        raise KeyError(f"Key {key} not found")

    # ---------- REPR ----------
    def repr(self):
        items = []
        for bucket in self._table:
            items.extend(bucket)
        return "HashTable{" + ", ".join(f"{k}: {v}" for k, v in items) + "}"

    ht = HashTable()

    ht["a"] = 10
    ht["b"] = 20
    ht["c"] = 30

    print(ht["a"])  # 10
    print(ht["b"])  # 20

    print(len(ht))  # 3

    ht.pop("b")

    print(ht)