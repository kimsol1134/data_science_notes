# 1 기준으로 스플릿
# 첫번째나 마지막이 0이면
# 0개수 2개일때마다 1개 심을수있음
# 나머지 칸에는 0개수 3개일때마다 1개 심을수 있음
# 심을수있는 갯수 >= n 이면 True 
# 문제점 발견 -> 1이 없는경우에 문제 생김 조건 추가함

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        place = 0
        if flowerbed.count(1) == 0:
            if (len(flowerbed)+1) // 2 >= n:
                return True
            else :
                return False 
        elif flowerbed[0] == 0 and flowerbed[-1] != 0:
            flowerbed = ''.join(str(x) for x in flowerbed)
            flowerbed = flowerbed.split("1")
            place += len(flowerbed[0])//2
            for w in flowerbed[1:]:
                if w != "":
                    place += (len(w)-1)//2
        elif flowerbed[0] != 0 and flowerbed[-1] == 0:
            flowerbed = ''.join(str(x) for x in flowerbed)
            flowerbed = flowerbed.split("1")
            place += len(flowerbed[-1])//2
            for w in flowerbed[:-1]:
                if w != "":
                    place += (len(w)-1)//2
        elif flowerbed[0] == 0 and flowerbed[-1] == 0:
            flowerbed = ''.join(str(x) for x in flowerbed)
            flowerbed = flowerbed.split("1")
            place += len(flowerbed[0])//2            
            place += len(flowerbed[-1])//2
            for w in flowerbed[1:-1]:
                if w != "":
                    place += (len(w)-1)//2
        else :
            flowerbed = ''.join(str(x) for x in flowerbed)          
            flowerbed = flowerbed.split("1")
            for w in flowerbed:
                if w != "":
                    place += (len(w)-1)//2

        if place >= n :
            return True
        else :
            return False