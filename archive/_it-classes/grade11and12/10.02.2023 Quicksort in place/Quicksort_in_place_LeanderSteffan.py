import random

class Quicksort:
    def __init__(self, liste):
        self.liste = liste
        bi, ei = 0, len(liste) - 1

    def quicksort_ip(self, bi, ei):
        if ei - bi > 0:
            pivot = self.liste[ei]
            pivot_i = ei
            i = bi
            while i >= bi and i < ei and pivot_i >= bi and i < pivot_i:
                if self.liste[i] >= pivot:
                    temp = self.liste[i]
                    for j in range(i, pivot_i):
                        self.liste[j] = self.liste[j + 1]
                    self.liste[pivot_i] = temp
                    pivot_i -= 1
                else:
                    i += 1
            self.quicksort_ip(bi, pivot_i - 1)
            self.quicksort_ip(pivot_i + 1, ei)
        else:
            pass

    def quicksort_ip_rode(self, bi, ei):
        if ei - bi > 0:
            pivot = self.liste[ei]
            pivot_i = ei
            g, k = bi, pivot_i - 1
            while g <= k and k >= bi and not g < 0 and not k == pivot_i:
                while self.liste[k] > pivot and g <= k:
                    k -= 1
                while self.liste[g] <= pivot and g <= k:
                    g += 1
                if g <= k  and self.liste[g] >= pivot and self.liste[k] <= pivot:
                    self.liste[k], self.liste[g] = self.liste[g], self.liste[k]
                    k -= 1
                    g += 1

            self.liste[pivot_i], self.liste[g] = self.liste[g], self.liste[pivot_i]
            pivot_i = g
            self.quicksort_ip_rode(bi, pivot_i - 1)
            self.quicksort_ip_rode(pivot_i + 1, ei)
        else:
            pass


random_list = random.sample(range(0, 1001), 1000)
test = Quicksort(random_list)
test.quicksort_ip_rode(0, len(test.liste) - 1)
print(test.liste)
