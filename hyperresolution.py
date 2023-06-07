from copy import deepcopy

# input nucleus
main_clause_input = input('Enter nucleus: ') 
main_clause = [int(x) for x in main_clause_input.split(",")]

main_dict = {}
for ele in main_clause:
    main_dict[ele] = ele

print("The nucleus is {}".format(main_clause))
print("Here the priority of literals is 1<2<3<4<5<6...")

# input sub clauses number
sub_clause_input = int(input('Enter number of sub clauses: ')) 
sub_clauses = []

# input sub clauses
for i in range(sub_clause_input): 
  sub_clause_input = input("Enter sub clause:{}".format(i+1))
  sub_clause_input_parsed = [int(x) for x in sub_clause_input.split(",")]
  sub_clauses.append(sub_clause_input_parsed)

print("The list of all negative clauses is {}".format(sub_clauses))

# sort sub clauses 
for i in range(0, len(sub_clauses)): 
  sub_clauses[i].sort()
sub_clauses.sort()
print("Negative clauses after sorting: {}".format(sub_clauses))


main_clause_temp = deepcopy(main_clause)

#sorted main clause
main_clause_sorted = sorted(main_clause_temp, reverse = True)

def check_number_exists(input):
  flag = 1
  for main_clause_val in main_clause_sorted:
    for sub_clause in sub_clauses:
      if input in sub_clause:
        flag = 0
  return flag


if -(sub_clauses[0][0]) not in main_clause:
  print("No new clauses can be obtained as highest priority literal in subclause {} is not present in nucleus".format(sub_clauses[0][0]))
  print("Final clauses after ordered hyperresolution: {}".main_clause)
else:
  queue = []
  queue.append(main_clause_sorted)
  final_clauses = set()
  y = sub_clauses.copy()
  for current_main_clause_value in main_clause_sorted:

      # sub_clauses_store = sub_clauses.copy()
      # y = sub_clauses.copy()
      if current_main_clause_value > 0: #10
        # if current_main_clause_value not in (item for sublist in y for item in sublist):
        #   break
        # print(current_main_clause_value)
        # print(check_number_exists(current_main_clause_value))
        if not (check_number_exists(current_main_clause_value)): 
          break
        while(len(queue) != 0):
            temp_que = []
            size_q = len(queue)
            y = deepcopy(sub_clauses)
            # y1 = y.copy()
            # print('initial y: ', y)
            # print('initial y1: ', y1)
            while size_q > 0:
                # print('que', queue)
                # print(sub_clauses)
                current_main_clause = queue.pop(0) #10, 9, 8
                #print(current_main_clause)
                # print(sub_clauses_store)
                sub_clauses = deepcopy(y)
                # print('y:', y)
                # [[-10, -9], [-9, -8], [-9, -2], [-8, -1]]
                set_te = set() 
                for idx, sub_clause in enumerate(sub_clauses): 
                    store_main_clause = current_main_clause.copy() # 10, 9, 8
                    # set_te.add(tuple(store_main_clause))
                    # print(current_main_clause, 'sub clause', sub_clause) # 10, 9,8
                    if -(current_main_clause_value) in sub_clause:  # -10 in [-10, -9] -> yes
                        if current_main_clause_value in store_main_clause: # 10 in [10, 9, 8] -> yes
                          store_main_clause.remove(current_main_clause_value) # store_main_clause = 9, 8
                        
                        # if any(val1 > 0 for val1 in store_main_clause):
                        #   print('store', store_main_clause)
                        set_te.add(tuple(store_main_clause)) # {(8)}

                        for sub_clause_value in sub_clause: # [-9, -2]
                            xx = list(store_main_clause).copy() # xx = [8]
                            # print(xx)
                            if sub_clause_value == -(current_main_clause_value):
                              continue
                            if -(sub_clause_value) in store_main_clause:
                              continue
                            if sub_clause_value not in store_main_clause: # -2 not in [8]
                              # print(sub_clause_value)
                              xx.append(sub_clause_value) # [8, -2]
                              sub_clause.remove(sub_clause_value)
                              # print(xx)
                              set_te.add(tuple(xx)) # {(8), (8, -2)}
                        # print(set_te)
                        
                        sub_clause.remove(-(current_main_clause_value))
                        # for val in set_te:
                        #   for val1 in list(val): 
                        #     if val1 == current_main_clause_value:
                        #       val.remove(-(current_main_clause_value)) 
                # print('set', set_te)
                for val in set_te:
                  # print('val: ', val)
                  if all(val1 < 0 for val1 in val): 
                    # print('here')
                    final_clauses.add(tuple(val))
                # print(final_clauses)
                # sub_clauses = y.copy()
                size_q = size_q -1

                
              
        queue.extend([list(subset) for subset in set_te if any(subset) > 0])

  # for val in sub_clauses: 
  #   if all(val1 < 0 for val1 in val): 
  #     final_clauses.add(tuple(val))

  # print(sub_clauses)
  # # print(queue)
  if len(final_clauses) == 0: final_clauses.add(tuple(main_clause))

  print("Final clauses after ordered hyperresolution: {}".format([list(item) for item in set(list(final_clauses))]))
        # temp_set.add(tuple(store_main_clause))
