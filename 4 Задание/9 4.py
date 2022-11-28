def Zadanie(n):
    q1 = 0
    q2 = 1
    q3 = 1
    w = 3
    s = 2
    if n == 1:
        print(0)
    else:
        if n == 2:
            print(1)
        else:
            if n == 3:
                print(2)
            else:
                while n > w:
                    if q1 < q2 and q1 < q3:
                        q1 = q2 + q3
                        s += q1
                        w += 1
                    else:
                        if q2 < q1 and q2 < q3:
                            q2 = q1 + q3
                            s += q2
                            w += 1
                        else:
                            if q3 < q1 and q3 < q2:
                                q3 = q1 + q2
                                s += q3
                                w += 1
                            else:
                                if (q1 < q2 and q1 == q3) or (q1 == q2 and q1 < q3):
                                    q1 = q2 + q3
                                    s += q1
                                    w += 1
                                else:
                                    if (q2 < q1 and q2 == q3) or (q2 == q1 and q2 < q3):
                                        q2 = q1 + q3
                                        s += q2
                                        w += 1
                                    else:
                                        if (q3 < q1 and q2 == q3) or (q3 == q1 and q3 < q2):
                                            q3 = q1 + q2
                                            s += q3
                                            w += 1
                print(s)
