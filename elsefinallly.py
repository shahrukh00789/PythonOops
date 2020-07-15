file1 = open("testfile.txt")

try:
    file2 = open("testfile3.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    file1.close()
    # file2.close()

print("Important Stuff")

