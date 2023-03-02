class Book:
    def __init__(self,name,author):
        try:
            with open("LibraryData.txt","r") as fp :
                all =[]
                for line in fp:
                    line = line.split(',')
                    all.append(line)
                if (len(all) > 0):
                    self.id = int(all[-1][0])+1
                    self.name = name
                    self.author = author
                else:
                    self.id = 100
                    self.name = name
                    self.author = author
        except FileNotFoundError:
            print("File does not exist")        

    def __str__(self):
        data = str(self.id)+','+self.name+','+self.author+','+str('1')+','+str('N/I')+','+str('-')
        return data