class Solution:
    def find_integer(self,arr, num):
        """
        :param arr: [[]]
        :param num: int
        :return: bool
        """
        if not arr:
            return False
        rows, cols = len(arr), len(arr[0])
        row, col = rows - 1, 0
        while row >= 0 and col <= cols - 1:
            if arr[row][col] == num:
                return True
            elif arr[row][col] > num:
                row -= 1
            else:
                col += 1
        return False

if __name__=='__main__':
    target=2
    array=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
    solution=Solution()
    ans=solution.find_integer(array,target)
    print(ans)
