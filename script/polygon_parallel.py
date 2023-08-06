#!/usr/bin/python3
import math

#points_in = [[2,2],[6,2],[2,-2],[-2,-2],[-2,2]]
points_in = [[1.000000,0.00],[0.998459,0.001476],[0.993844,0.002120],[0.986185,0.003182],[0.975528,0.004642],[0.961940,0.006478],[0.945503,0.008658],[0.926320,0.011149],[0.904508,0.013914],[0.880203,0.016914],[0.853553,0.020107],[0.824724,0.023452],[0.793893,0.026905],[0.761249,0.030423],[0.726995,0.033962],[0.691342,0.037476],[0.654508,0.040917],[0.616723,0.044237],[0.578217,0.047383],[0.539230,0.050302],[0.500000,0.052940],[0.460770,0.055241],[0.421783,0.057148],[0.383277,0.058609],[0.345492,0.059575],[0.308658,0.060000],[0.273005,0.059848],[0.238751,0.059092],[0.206107,0.057714],[0.175276,0.055709],[0.146447,0.053083],[0.119797,0.049854],[0.095492,0.046049],[0.073680,0.041705],[0.054497,0.036867],[0.038060,0.031580],[0.024472,0.025893],[0.013815,0.019854],[0.006156,0.013503],[0.001541,0.006877],[0.000000,0.000000],[0.001541,-0.006877],[0.006156,-0.013503],[0.013815,-0.019854],[0.024472,-0.025893],[0.038060,-0.031580],[0.054497,-0.036867],[0.073680,-0.041705],[0.095492,-0.046049],[0.119797,-0.049854],[0.146447,-0.053083],[0.175276,-0.055709],[0.206107,-0.057714],[0.238751,-0.059092],[0.273005,-0.059848],[0.308658,-0.060000],[0.345492,-0.059575],[0.383277,-0.058609],[0.421783,-0.057148],[0.460770,-0.055241],[0.500000,-0.052940],[0.539230,-0.050302],[0.578217,-0.047383],[0.616723,-0.044237],[0.654508,-0.040917],[0.691342,-0.037476],[0.726995,-0.033962],[0.761249,-0.030423],[0.793893,-0.026905],[0.824724,-0.023452],[0.853553,-0.020107],[0.880203,-0.016914],[0.904508,-0.013914],[0.926320,-0.011149],[0.945503,-0.008658],[0.961940,-0.006478],[0.975528,-0.004642],[0.986185,-0.003182],[0.993844,-0.002120],[0.998459,-0.001476]];


def vec2d_perpendicular(Vec, Dir = 'right'):
    return [Vec[1], -Vec[0]] if Dir == 'right' else [-Vec[1], Vec[0]]

def vec2d_unit(Vec):
    abs_len = math.sqrt(Vec[0]**2 + Vec[1]**2)
    return [Vec[0]/abs_len, Vec[1]/abs_len]

def line_intersection(P1, Vec1, P2, Vec2):
    X0A = P1[0]
    Y0A = P1[1]
    XsA = Vec1[0]
    YsA = Vec1[1]
    X0B = P2[0]
    Y0B = P2[1]
    XsB = Vec2[0]
    YsB = Vec2[1]

    U1 = XsA*(Y0B-Y0A) + YsA*(X0A-X0B)
    U2 = XsB*YsA - XsA*YsB

    if U2 == 0: #colinear lines
        return None
    
    U = U1/U2
    #print ("U1 U2 U:", U1, U2, U)

    Xits = X0B + U*XsB
    Yits = Y0B + U*YsB

    return [round(Xits, 6), round(Yits, 6)]

# segment: Sx = [[x0,y0],[x1,y1]]
def line_segments_intersection(S1, S2):
    A = S1[0]
    B = S1[1]
    C = S2[0]
    D = S2[1]
    T = line_intersection(A, [B[0]-A[0], B[1]-A[1]], C, [D[0]-C[0], D[1]-C[1]])
    if T is None:
        return None
    #if point lies out of segmet, return None
    Min = min(A[0],B[0])
    Max = max(A[0],B[0])
    if T[0] < Min or T[0] > Max:
        return None   #out of range
    Min = min(A[1],B[1])
    Max = max(A[1],B[1])
    if T[1] < Min or T[1] > Max:
        return None  #out of range
    Min = min(C[0],D[0])
    Max = max(C[0],D[0])
    if T[0] < Min or T[0] > Max:
        return None   #out of range
    Min = min(C[1],D[1])
    Max = max(C[1],D[1])
    if T[1] < Min or T[1] > Max:
        return None  #out of range
    return T

def triangle_area_with_orientation(points):
    P0, P1, P2 = points
    #(1/2) |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|
    return (P0[0]*(P1[1] - P2[1]) + P1[0]*(P2[1] - P0[1]) + P2[0]*(P0[1] - P1[1])) / 2  #ignore sign to get also negative values

def polygon_area_with_orientation(points):
    area2 = 0
    P0 = points[0]
    for i in range(1, len(points)-1):
        P1 = points[i]
        P2 = points[i+1]
        #triangle area = (1/2) |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|
        area2 += P0[0]*(P1[1] - P2[1]) + P1[0]*(P2[1] - P0[1]) + P2[0]*(P0[1] - P1[1])
    return area2 / 2

def split_self_intersecting_polygon(points):
    segments = list()
    for i in range(0, len(points)-2):
        segments.append([points[i], points[i+1]])
    segments.append([points[i+1], points[0]])

    polygons = list()
    for i in range(0, len(segments)-1):


    return polygons

def polygon_offset(points, distance):
    points.append(points[0]) #make first point also last one
    points_mv = []
    dir_vect = []
    points_out = []

    for i in range(len(points)-1):
        ptA = points[i]
        ptB = points[i+1]
        vec_dir = [ptB[0]-ptA[0], ptB[1]-ptA[1]] #direction vector of the segment
        vec_norm = vec2d_unit(vec2d_perpendicular(vec_dir))
        vec_move = [distance*vec_norm[0], distance*vec_norm[1]]
        pt_mv = [ptA[0]+vec_move[0], ptA[1]+vec_move[1]] #moved point
        print (ptA , pt_mv)
        
        points_mv.append([ptA[0]+vec_move[0], ptA[1]+vec_move[1]])
        dir_vect.append(vec_dir)

    points_mv.append(points_mv[0])  #make first also last
    dir_vect.append(dir_vect[0])    #make first also last

    for i in range(len(points_mv)-1):
        pt_intersection = line_intersection(points_mv[i], dir_vect[i], points_mv[i+1], dir_vect[i+1])
        if pt_intersection is not None:
            points_out.append(pt_intersection)
            print (pt_intersection)

    return points_out

#pp = polygon_offset(points_in, -0.03)
#print (pp)
#print ('[' + ','.join(pp) + ']')

#triangle = [[0,0],[0,3],[2,0]]
#print(triangle_area_with_orientation(triangle))

#pts = [[0,0],[0,3],[-2,0],[-1,1]]
#print(polygon_area_with_orientation(pts))
#pts = [[0,0],[0,3],[-2,0],[-1,-1]]
#print(polygon_area_with_orientation(pts))

S1 = [[0,1],[5,1]]
S2 = [[2,3],[2,-3]]
print(line_segments_intersection(S1,S2))
S1 = [[0,6],[6,0]]
S2 = [[0,0],[6,6]]
print(line_segments_intersection(S1,S2))
S1 = [[0,6],[6,0]]
S2 = [[0,0],[-6,-6]]
print(line_segments_intersection(S1,S2))
S1 = [[0,4],[4,0]]
S2 = [[0,0],[2,2]]
print(line_segments_intersection(S1,S2))