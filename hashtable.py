
class HashTable:
    def __init__(self, initial_size=5):
        self.lst = [None] * initial_size

    def put(self, k, v):
        current = self.lst[k % len(self.lst)]
        if current is None:
            current = []

        for i in range(len(current)):
            if current[i][0] == k:
                current.remove(current[i])
                break

        current.append((k,v))
        self.lst[k % len(self.lst)] = current

    def get(self, k):
        current = self.lst[k % len(self.lst)]

        if current is not None:
            for key, value in current:
                if key == k:
                    return value

        return None

    def __len__(self):
        cnt = 0
        for x in self.lst:
            if x is not None:
                cnt += len(x)
        return cnt

    def rebalance(self):
        new_lst = [None] * len(self)

        for x in self.lst:
            if x is not None:
                for k, v in x:
                    new_curr = new_lst[ k % len(new_lst) ]
                    if new_curr is None:
                        new_curr = []
                    new_curr.append((k, v))
                    new_lst[k % len(new_lst)] = new_curr

        self.lst = new_lst

    def list(self):
        s = '['
        for xs in self.lst:
            if xs is not None:
                for k, v in xs:
                    s += '(' + str(k) + ', ' + str(v) + '), '
        s += ']'
        return s
