def paint_billboards(K, T, lengths):
    n = len(lengths)
    
    def can_paint(time):
        painters = 1
        current_length = 0
        
        for i in range(n):
            if lengths[i] > time:
                return False
            if current_length + lengths[i] <= time:
                current_length += lengths[i]
            else:
                painters += 1
                current_length = lengths[i]
                
        return painters <= K

    left, right = max(lengths), sum(lengths)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_paint(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return result * T

