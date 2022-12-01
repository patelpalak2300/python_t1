# 126.
# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(6):
#     for j in range(i):
#         print("*",end =" ")
#     print()

#127.
# * * * * * 
#   * * * *
#     * * *
#       * *
#         * 

# for i in range(6):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for k in range(5,i,-1):
#         print("*",end=" ")
#     print()

#
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

# for i in range(6):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(5,i,-1):
#         print("*",end=" ")
#     print()

# 128.
#     *
#    * * 
#   * * *
#  * * * *
# * * * * *
# for i in range(6):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for k in range(0,i):
#         print("*",end=" ")
#     print()

#129.
# * * * * 
# * * *
# * *
# *
# for i in range(4):
#     for j in range(4,i,-1):
#         print("*",end=" ")
#     print()

# 130.
# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for i in range(5,0,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()

#131

# 1 
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 132
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# 133
# * 
# # #
# * * *
# # # # #
# for i in range(1,5):
#     for j in range(1,i+1):
#         if(i%2==0):
#             print("#",end=" ")
#         else:
#             print("*",end=" ")
#     print()
# 134
# 1 
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# for i in range(1,6):
#     for j in range(1,i+1):
#       if(i%2==0):
#         if(j%2==0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#       else:
#         if(j%2==1):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")

#     print()
#

#135
#         1   
#       1   2
#     1   2   3
#   1   2   3   4
# 1   2   3   4   5

# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k," ",end=" ")
#     print()


#136
#         1   
#       2   2
#     3   3   3
#   4   4   4   4
# 5   5   5   5   5
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(i," ",end=" ")
#     print()

#137
#         1   
#       1   2
#     1   2   3
#   1   2   3   4

# for i in range(1,5):
#     for j in range(5,i,-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()

#137
#           *   
#         #   #
#       *   *   *
#     #   #   #   #
#   *   *   *   *   *

for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end="")
    for k in range(0,i):
        if(i%2==0):
            print("#",end=" ")
        else:
            print("*",end=" ")
    print()
    

