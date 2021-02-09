import heapq

class Ratings(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        ax, ay = self.val[0], self.val[1]
        bx, by = other.val[0], other.val[1]
        # print(ax, ay)
        # print(bx, by)
        res= -( (ax+1)/(ay+1) - ax/ay) <= -( (bx+1)/(by+1) - bx/by )
        #print(res)
        return res

# def printHeap(heap):
#     while heap:
#         r = heapq.heappop(heap)
#         print(r.val[0], r.val[1])


def fiveStarSellers(ratings, threshold):

    avgRatings = 0
    total5Stars, N = 0, 0
    count = 0
    N = len(ratings)
    for i, rating in enumerate(ratings):
        total5Stars += rating[0]/ rating[1]
        ratings[i] = Ratings(rating)
    print(total5Stars)
    avgRatings = total5Stars/N
    print(avgRatings)
    print(ratings)
    # Heapify the ratings array
    heapq.heapify(ratings)

    while avgRatings < threshold and ratings:
        r = heapq.heappop(ratings)

        avgRatings += ( ( (r.val[0]+1)/(r.val[1]+1) ) - r.val[0]/r.val[1] )/N
        r.val[0] += 1
        r.val[1] += 1

        heapq.heappush(ratings, r)

        count += 1
        print()
    return count
    #printHeap(ratings)


#print(fiveStarSellers([[4,4], [1,2], [3,6]], 0.77))
# print(fiveStarSellers([[9, 10]], 0.91))
print((fiveStarSellers([[1,2], [2,3]], 0.75)))