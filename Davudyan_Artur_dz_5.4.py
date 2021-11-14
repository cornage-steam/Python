my_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

lst_comp = [j for i, j in enumerate(my_lst) if i != 0 and j > my_lst[i - 1]]
print(lst_comp)
