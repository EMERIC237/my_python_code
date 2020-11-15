def dec_to_bin(num):

    if num > 1:
        dec_to_bin(num//2)
    print(num%2, end='')



def bin_to_dec(num):
    dec_value = 0
    s_num = str(num)
    e=len(s_num)-1
    for i in s_num:
        dec_value = (int(i))*(2**e)+dec_value
        e-=1
    print(dec_value)

def main():
	answer = input("Do you want to move: \n  from decimal to binary\n  or from binary to decimal\nchoose 'one' for the first option and 'two' for the second option " )
	if answer == "one" or answer == "1":
		print("Good choice")
		print("You choosed from decimal to binary")
		number=int(input("write the value you want to convert "))
		dec_to_bin(number)
	elif answer == "two" or answer == "2":
		print("Good choice")
		print("You choosed from binary to decimal")
		number=int(input("write the value you want to convert "))
		bin_to_dec(number) 
	else:
		print("you choosed the wrong choice\nPlease,choose 'one' for option 1 or 'two' for option 2" )
		main()


if __name__=="__main__":
	main()
