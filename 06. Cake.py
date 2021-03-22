wi = int(input())
le = int(input())
total_pieces = wi * le
command = input()
while command != "STOP":
    cur_peaces = int(command)
    total_pieces -= cur_peaces
    if total_pieces < 0:
        break
    command = input()

if total_pieces >= 0:
    print (f"{total_pieces} pieces are left.")
else:

    print (f"No more cake left! You need {abs(total_pieces)} pieces more.")

