class FileManager:
    def __init__(self, filename, result, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.result = result
 
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self

    def Calc(self):
        # x = 1 / 0
        print("1000")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()        

        print("Anyway1")
        # raise ValueError("Test error")

        print("Anyway2")
        print(exc_type, exc_val, exc_tb)
        return self.result

# Usage
with FileManager("data.txt", False, "r") as f:
    f.Calc()
    if f.file is not None:
        for line in f.file:
            print(line.rstrip("\n"))

print("continue")