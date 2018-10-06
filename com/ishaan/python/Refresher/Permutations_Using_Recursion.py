class Curr:
    count = 0


    @staticmethod
    def perm(names, prefix):
        if names == "":
            Curr.count += 1
            if Curr.count%1 == 0 :
                print("prem number {} is {}".format(Curr.count, prefix))
            return
        for i in range(len(names)):
            Curr.perm(names[:i] + names[i + 1:], names[i] + prefix)


Curr.perm("PreetiKul","")