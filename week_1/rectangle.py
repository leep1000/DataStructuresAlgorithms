def area(rec1, rec2, rec3):
    rec1_area = abs(rec1[0] - rec1[2]) * abs(rec1[1] - rec1[3])
    rec2_area = abs(rec2[0] - rec2[2]) * abs(rec2[1] - rec2[3])
    rec3_area = abs(rec3[0] - rec3[2]) * abs(rec3[1] - rec3[3])
    print(rec1_area)
    print(rec2_area)
    print(rec3_area)
    
    area = max(rec1_area, rec2_area, rec3_area)
    
    if rec1_area > rec2_area and rec1_area > rec3_area:
        if rec1[0] != rec2[0] or rec1[2] != rec2[2]:
    

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16