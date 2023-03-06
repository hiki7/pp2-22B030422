with open(r"C:/temp/kbtu stuff/test/test.txt", "r") as fp:
    lines = len(fp.readlines())
    print("Number of lines:", lines)