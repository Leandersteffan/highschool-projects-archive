class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = max(count, self.dfs(grid, i, j))
        return count


    def dfs(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[i]) or j < 0 or i < 0 or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        count = 1
        count += self.dfs(grid, i - 1, j)
        count += self.dfs(grid, i + 1, j)
        count += self.dfs(grid, i, j - 1)
        count += self.dfs(grid, i, j + 1)
        return count


# zweiter Versuch von mir
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        every, had_index, base_index, old_base_index, row_len, x, clip, out = [], [], [], [], len(grid[0]), 1, 0, 0
        for i in range(len(grid)):
            for j in range(row_len):
                every.append(grid[i][j])
        #print(every)
        for i in range(len(every)):
            #print('neu i', row_len)
            if i not in had_index:
                clip = 1
                if every[i] == 1:
                    had_index.append(i)
                    base_index.clear()
                    base_index.append(i)
                    x = 1
                    while i + x < len(every) and every[i + x] == 1:
                        had_index.append(i + x)
                        base_index.append(i + x)
                        x += 1
                        clip += 1
                    while len(base_index) != 0 and max(base_index) + row_len <= len(every):
                        #print(base_index)
                        for k in range(len(base_index)):
                            or_to_old = base_index.pop(0)
                            old_base_index.append(or_to_old)
                        #print(old_base_index)
                        for base in old_base_index:
                            #print('base', base)
                            if base + row_len < len(every) and every[base + row_len] == 1:
                                l = (base + row_len) / row_len
                                min_row_index = int(l) * row_len
                                max_row_index = int(l + 1)* row_len
                                #print(min_row_index, max_row_index)
                                if base + row_len not in had_index:
                                    had_index.append(base + row_len)
                                    base_index.append(base + row_len)
                                    clip += 1
                                    x = 1
                                    while base + row_len - x >= min_row_index and every[base + row_len - x] == 1:
                                        had_index.append(base + row_len - x)
                                        base_index.append(base + row_len - x)
                                        x += 1
                                        clip += 1
                                    x = 1
                                    while base + row_len + x < len(every) and base + row_len + x <= max_row_index and every[base + row_len + x] == 1:
                                        had_index.append(base + row_len + x)
                                        base_index.append(base + row_len + x)
                                        x += 1
                                        clip += 1
                                if base - row_len not in had_index and base - row_len > 0 and every[base - row_len] == 1:
                                    had_index.append(base - row_len)
                                    base_index.append(base - row_len)
                                    clip += 1
                                    x = 1
                                    while base - row_len - x >= min_row_index and every[base - row_len - x] == 1:
                                        had_index.append(base - row_len - x)
                                        base_index.append(base - row_len - x)
                                        x += 1
                                        clip += 1
                                    x = 1
                                    while base - row_len + x <= max_row_index and every[base - row_len + x] == 1:
                                        had_index.append(base - row_len + x)
                                        base_index.append(base - row_len + x)
                                        x += 1
                                        clip += 1
                        old_base_index.clear()
                    #print(clip)
                    out = max(clip, out)
        return out


# von mir aber zu langsam
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ones = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones.append([i, j])
                    ones.append('-')
        for i in range(len(ones)):
            for j in range(i + 1, len(ones)):
                if type(ones[i]) == list and type(ones[j]) == list:
                    if ones[i][0] == ones[j][0]:
                        if ones[i][1] == ones[j][1] + 1 or ones[i][1] == ones[j][1] - 1:
                            x = ones.pop(j)
                            ones.insert(i, x)
        for i in range(len(ones)):
            for j in range(i + 1, len(ones)):
                if type(ones[i]) == list and type(ones[j]) == list:
                    if ones[i][1] == ones[j][1] and '-' in ones[i:j]:
                        if ones[i][0] == ones[j][0] + 1 or ones[i][0] == ones[j][0] - 1:
                            y, x, also_move = -1, 1, [j]
                            while True:
                                if type(ones[j + y]) == list:
                                    also_move.append(j + y)
                                    y -= 1
                                elif type(ones[j + x]) == list:
                                    also_move.append(j + x)
                                    x += 1
                                else:
                                    break
                            also_move.sort()
                            for k in range(len(also_move)):
                                c = ones.pop(also_move[k])
                                ones.insert(i + 1, c)
        clip, out = 0, 0
        for i in range(len(ones)):
            if type(ones[i]) == list:
                clip += 1
            else:
                out = max(clip, out)
                clip = 0
        return out
