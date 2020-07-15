def queue_time(customers, n):
    # TODO
    q=[]
    l=len(customers)
    if l==0:
      print("wrong answer for case with an empty queue")
      exit()
    elif l>n:
    
      for i in range(n):
        q.append(customers[i])
    else:
      for i in range(l):
        q.append(customers[i])
      max_q=q[0]
      for j in range(len(q)):
        if q[i]>max_q:
          max_q=q[i]
      return max_q
    del customers[0:n]
    for k in range(len(customers)):
        min_q=min(q)
        min_q_index=q.index(min_q)
        min_q=min_q+customers[k]
        q[min_q_index]=min_q
        min_q=0
    return max(q)
        
        
