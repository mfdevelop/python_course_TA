'''
num1, num2 = input().split()
    num1_d0 = bool(int(num1[0]))
    num1_d1 = bool(int(num1[1]))
    num1_d2 = bool(int(num1[2]))
    num1_d3 = bool(int(num1[3]))
    num2_d0 = bool(int(num2[0]))
    num2_d1 = bool(int(num2[1]))
    num2_d2 = bool(int(num2[2]))
    num2_d3 = bool(int(num2[3]))

    # f add 3
    c4 = bool(0)
    s3 = (num1_d3 != num2_d3) != c4
    c3 = (num1_d3 and num2_d3) or ((num1_d3 != num2_d3) and c4)

    # f add 2
    s2 = (num1_d2 != num2_d2) != c3
    c2 = (num1_d2 and num2_d2) or ((num1_d2 != num2_d2) and c3)

    # f add 1
    s1 = (num1_d1 != num2_d1) != c2
    c1 = (num1_d1 and num2_d1) or ((num1_d1 != num2_d1) and c2)

    # f add 0
    s0 = (num1_d0 != num2_d0) != c1
    c0 = (num1_d0 and num2_d0) or ((num1_d0 != num2_d0) and c1)

    main_sum = str(int(s0)) + str(int(s1)) + str(int(s2)) + str(int(s3))
    carry_out = str(int(c0))
    print(carry_out, main_sum)
'''

'''
    n, major_string = input().split()
    n = int(n)
    major_set = set(major_string)
    # for char in major_string:
    #     set_of_chars.add(char)
    answer = []
    for i in range(n):
        temp = set(input())
        if temp.issubset(major_set):
            answer.append("YES")
        else:
            answer.append("NO")
    for i in answer:
        print(i)
    
    tempt_string = input()
    tempt_string.replace(" ", "")
    tempt_string = tempt_string.lower()
    if tempt_string == tempt_string[::-1]:
        print("YES")
    else:
        print("NO")
'''
'''
    n = int(input())
    azla_list = []
    noghat_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        azla_list.append([((temp_list[0] - temp_list[2]) ** 2 + (temp_list[1] - temp_list[3]) ** 2) ** 0.5,
                          ((temp_list[0] - temp_list[4]) ** 2 + (temp_list[1] - temp_list[5]) ** 2) ** 0.5,
                          ((temp_list[2] - temp_list[4]) ** 2 + (temp_list[3] - temp_list[5]) ** 2) ** 0.5, ])
        noghat_list.append([*temp_list])
    res = []
    for i in range(n):
        if (noghat_list[i][0], noghat_list[i][1]) == (noghat_list[i][2], noghat_list[i][3]) or (
                noghat_list[i][0], noghat_list[i][1]) == (noghat_list[i][4], noghat_list[i][5]) or (
                noghat_list[i][2], noghat_list[i][3]) == (noghat_list[i][4], noghat_list[i][5]) or noghat_list[i][0] == \
                noghat_list[i][2] and noghat_list[i][2] == noghat_list[i][4]:
            res.append("not a ")
    
        else:
            if azla_list[i][0] == azla_list[i][1] and azla_list[i][1] == azla_list[i][2]:
                res.append("equilateral ")
            elif azla_list[i][1] == azla_list[i][2] or azla_list[i][0] == azla_list[i][2] or azla_list[i][1] == \
                    azla_list[i][0]:
                res.append("isosceles ")
            else:
                res.append("scalene ")
            azla_list[i].sort()
            print(azla_list[i][2])
            print(azla_list[i][1])
            print(azla_list[i][0])
            if azla_list[i][2] ** 2 == azla_list[i][0] ** 2 + azla_list[i][1] ** 2:
                res[i] += "right "
            elif azla_list[i][2] ** 2 > azla_list[i][0] ** 2 + azla_list[i][1] ** 2:
                res[i] += "obtuse "
            else:
                res[i] += "acute "
        res[i] += "triangle"
    
    for i in res:
        print(i)
'''
