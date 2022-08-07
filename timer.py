import time
def main():
    def timer(length):
        while length > 0:
            print(length/60)
            length -= 1
            time.sleep(1)
        else:
            print("time over")
    Raw_input = int(input("enter in the time in minutes here: "))
#Coverts input in minutes to seconds
    True_Val = Raw_input * 60
    timer(True_Val)

if __name__ == "__main__":
    main()
