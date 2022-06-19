#Parse data
'''
    Seats:
        -----row------   -left-  -right-   ABC    DEF
        [[[***], [***]], [[***], [***]], [[***], [***]]]
    Requirements:
        []

'''
def parse():
    n = int(input())
    seats = list()
    for v in range(n):
        seats.append(input().split('_'))
    m = int(input())
    req = list()
    for v in range(m):
        req.append(input().split())
        req[-1][0] = int(req[-1][0])
    return seats, req

def process_req(seats, requir):
