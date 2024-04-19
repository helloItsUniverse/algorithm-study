def solution(wallpaper):
    answer = []
    xs, ys1, ys2 = [], [], []
    row = len(wallpaper)
    col = len(wallpaper[0])
    print(f'{row}, {col}')
    
    # S(min_row_num, min_col_num) , E(Max_row_num, Max_col_num)
    
    i = 0
    for r in wallpaper:
        print(r.find('#'), r.rfind('#'))
        if r.find('#') == -1:
            i += 1
            continue
        ys1.append(r.find('#'))
        ys2.append(r.rfind('#'))
        xs.append(i)
        i += 1
    
    print()
    print(xs)
    print(ys1)
    print(ys2)
    print()
    
    lux = min(xs)
    luy = min(ys1)
    rdx = max(xs) + 1
    rdy = max(ys2) + 1
    answer = [lux, luy, rdx, rdy]
    
    return answer