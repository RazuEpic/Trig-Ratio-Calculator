import math as mh

while True:
    has_opp = input("""
[Does your trigonometry ratio use the opposite side length?]
[Know that, to get 100 gradian, you MUST use the opposite side length]
>>""")

    if has_opp.lower() in ["yes", "y", "yep", "yeah", "i guess"]:
        opp_len = int(input("[What is the length of the opposite side?]\n>>"))
        adj_or_hyp = input("""
[Will you use the adjacent side or use the hypotenuse? (adj or hyp)]
[To get an answer of 100 gradian, you must answer hypotenuse.]
>>""")
        if adj_or_hyp.lower() in ["hyp", "hypotenuse"]:
            hyp_len = int(input("""
[What is the length of your hypotenuse?]
[In order to get an answer of 100 gradian, the value of your hypotenuse must be the same as your opposite length.]
>>"""))
            if hyp_len < opp_len:
                print("[Hypotenuse must be equal to or greater than the opposite side length.]")
            else:
                rad_sin = mh.asin(opp_len/hyp_len)
                deg_sin = mh.degrees(rad_sin)
                grad_a = deg_sin * (10 / 9)
                grad_ar = round(grad_a, 0)
                print(f"{grad_ar} gradian.")
                break
        else:
            adj_len = int(input("""
[What is the length of your adjacent side length?]        
>>"""))
            rad_tan = mh.atan(opp_len / adj_len)
            deg_tan = mh.degrees(rad_tan)
            grad_b = deg_tan * (10 / 9)
            grad_br = round(grad_b, 0)
            print(f"{grad_br} gradian.")
            break
    else:
        if has_opp.lower() in ["no", "n", "nope", "nah", "probably not"]:
            adj_len2 = int(input("[What is the adjacent side length?]\n>>"))
            hyp_len2 = int(input("[What is the hypotenuse side length?]\n>>"))
            if hyp_len2<adj_len2:
                print("[Hypotenuse must be equal to or greater than the adjacent side length.]")
            else:
                rad_cos = mh.acos(adj_len2 / hyp_len2)
                deg_cos = mh.degrees(rad_cos)
                grad_c = deg_cos * (10 / 9)
                grad_cr = round(grad_c, 0)
                print(f"{grad_cr} gradian.")
                break
        else:
            print("[Initial input must be 'yes' or 'no'. Any other parameters are invalid.]")
