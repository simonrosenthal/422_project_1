def find_turn(x1, y1, x2, y2, x3, y3):
    """
    x1 = before_pt.lon
    y1 = before_pt.lat
    x2 = turn_pt.lon
    y2 = turn_pt.lat
    x3 = after_pt.lon
    y3 = after_pt.lat
    """

    if x2 - x1 == 0:
        """ turnpoint on the y-axis """
        if y2 - y1 > 0:
            if x3 - x2 == 0:
                return "something wrong, it might be a straight line"
            elif (y3-y2)/(x3-x2) >= 0:
                if y3-y2 >= 0:
                    return "right"
                else:
                    return "left"
            else:
                if y3-y2 > 0:
                    return "left"
                else:
                    return "right"
        else:
            if x3 - x2 == 0:
                return "something wrong, it might be a straight line"
            elif (y3-y2)/(x3-x2) >= 0:
                if y3-y2 >= 0:
                    return "left"
                else:
                    return "right"
            else:
                if y3-y2 > 0:
                    return "right"
                else:
                    return "left"
    else:
        if (y2-y1)/(x2-x1) >= 0:
            if y2-y1 > 0:
            # turnpoint in first quadrant
                if x3-x2 == 0:
                    if y3-y2 > 0:
                        return "left"
                    else:
                        return "right"
                elif (y3-y2)/(x3-x2) <= 0:
                    if y3-y2 > 0:
                        return "left"
                    elif y3-y2 < 0:
                        return "right"
                    else:
                        if x3-x2 < 0:
                            return "left"
                        else:
                            return "right"
                else:
                    if (y3-y2)/(x3-x2) < (y2-y1)/(x2-x1):
                        if x3-x2 > 0:
                            return "right"
                        else:
                            return "left"
                    else:
                        if x3-x2 > 0:
                            return "left"
                        else:
                            return "right"
            elif y2-y1 < 0:
            # turnpoint in third quadrant
                if x3-x2 == 0:
                    if y3-y2 > 0:
                        return "right"
                    else:
                        return "left"
                elif (y3-y2)/(x3-x2) <= 0:
                    if y3-y2 > 0:
                        return "right"
                    elif y3-y2 < 0:
                        return "left"
                    else:
                        if x3-x2 < 0:
                            return "right"
                        else:
                            return "left"
                else:
                    if (y3-y2)/(x3-x2) < (y2-y1)/(x2-x1):
                        if x3-x2 > 0:
                            return "left"
                        else:
                            return "right"
                    else:
                        if x3-x2 > 0:
                            return "right"
                        else:
                            return "left"
            else:
            # turnpoint on the x-axis
                if x2-x1 > 0:
                    if y3-y2 > 0:
                        return "left"
                    elif y3-y2 < 0:
                        return "right"
                    else:
                        return "something wrong, it might be a straight line"
                elif x2-x1 < 0:
                    if y3-y2 > 0:
                        return "right"
                    elif y3-y2 < 0:
                        return "left"
                    else:
                        return "something wrong, it might be a straight line"
        else:
            if y2-y1 > 0:
            # turnpoint in second quadrant
                if x3-x2 == 0:
                    if y3-y2 > 0:
                        return "right"
                    else:
                        return "left"
                elif (y3-y2)/(x3-x2) >= 0:
                    if y3-y2 > 0:
                        return "right"
                    elif y3-y2 < 0:
                        return "left"
                    else:
                        if x3-x2 < 0:
                            return "left"
                        else:
                            return "right"
                else:
                    if (y3-y2)/(x3-x2) < (y2-y1)/(x2-x1):
                        if x3-x2 > 0:
                            return "left"
                        else:
                            return "right"
                    else:
                        if x3-x2 > 0:
                            return "right"
                        else:
                            return "left"
            elif y2-y1 < 0:
            # turnpoint in fourth quadrant
                if x3-x2 == 0:
                    if y3-y2 > 0:
                        return "left"
                    else:
                        return "right"
                elif (y3-y2)/(x3-x2) >= 0:
                    if y3-y2 > 0:
                        return "left"
                    elif y3-y2 < 0:
                        return "right"
                    else:
                        if x3-x2 < 0:
                            return "right"
                        else:
                            return "left"
                else:
                    if (y3-y2)/(x3-x2) < (y2-y1)/(x2-x1):
                        if x3-x2 > 0:
                            return "right"
                        else:
                            return "left"
                    else:
                        if x3-x2 > 0:
                            return "left"
                        else:
                            return "right"
                            
                            
                            
                            
                            
if __name__ == '__main__':

    print(find_turn(0, 0, 3, 1, 2, 7)) #left
    print(find_turn(1, 1, 3, 1, 3, -3)) #right
    print(find_turn(0, 0, -1, -1, -3, 7)) #right
    print(find_turn(-3, 3, 0, 0, -3, 7)) #left
