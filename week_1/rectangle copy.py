def calculate_area(rectangles):
    # Define events
    OPEN, CLOSE = 0, 1
    events = []
    for (x1, y1, x2, y2) in rectangles:
        events.append((x1, OPEN, y1, y2))
        events.append((x2, CLOSE, y1, y2))
    
    # Sort the events based on the x coordinate
    events.sort(key=lambda x: (x[0], -x[1]))

    active_intervals = []
    last_x = events[0][0]
    area = 0
    
    # Process the events
    for x, typ, y1, y2 in events:
        # Calculate the y coverage from the active intervals
        y_coverage = 0
        last_y = -float('inf')
        for y_start, y_end in sorted(active_intervals):
            y_start = max(y_start, last_y)
            if y_end > y_start:
                y_coverage += y_end - y_start
                last_y = y_end
        
        # Add the area covered since the last event
        area += y_coverage * (x - last_x)
        last_x = x
        
        # Add or remove the interval
        if typ == OPEN:
            active_intervals.append((y1, y2))
        else:
            active_intervals.remove((y1, y2))

    return area

def area(rec1, rec2, rec3):
    rectangles = [rec1, rec2, rec3]
    return calculate_area(rectangles)


    
    

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16