def area(rec1, rec2, rec3):
    rec1_area = abs(rec1[0] - rec1[2]) * abs(rec1[1] - rec1[3])
    rec2_area = abs(rec2[0] - rec2[2]) * abs(rec2[1] - rec2[3])
    rec3_area = abs(rec3[0] - rec3[2]) * abs(rec3[1] - rec3[3])
    print(rec1_area)
    print(rec2_area)
    print(rec3_area)
    
    total_area = rec1_area + rec2_area + rec3_area
    
    calculate_overlap(rec2, rec3)
    
    #total_overlap = calculate_overlap(rec1, rec2) + calculate_overlap(rec1, rec3) + calculate_overlap(rec2, rec3)
    #print(f"total overlap {total_overlap}")
    
    #return total_area - total_overlap
    
    
def calculate_overlap(rectangle1, rectangle2):
    overlap_width = abs(rectangle1[2] - rectangle2[2]) - abs(rectangle1[0] - rectangle2[0])
    overlap_height = abs(rectangle1[3] - rectangle2[3]) - abs(rectangle1[1] - rectangle2[1])
    if overlap_width > 0 and overlap_height > 0:
        print(f"overlap: {overlap_width * overlap_height}")
        return overlap_width * overlap_height
    else:
        return 0

    
    

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16