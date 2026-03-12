if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    scores = [i[1] for i  in students]
    unique_scores = sorted(list(set(scores)))
    second_lowest = unique_scores[1]
    
    result = [i[0] for i in students if i[1] == second_lowest]
    
    for j in sorted(result):
        print(j)
    
    
