ct=0
print("Números binarios:")
for b1 in range(0,1+1,1):
    for b2 in range(0, 1+1, 1):
        for b3 in range(0, 1+1, 1):
            ct += 1
            print(ct, "- ",b1, b2, b3, sep="")

            #ou print(f"{b1},{b2},{b3}")
            #ou print(str(b1) + str(b2) + str(b3))

