import os
import re
import web3

root = os.getcwd()  # address of current working directory

def find_func(file_name):
        f = open(file_name)
        stri = f.read()
        f.close()
        all_arg = ""
        read_f = open("rsult.txt","a+")
        r1 = re.findall("(function)[ ]([A-Za-z]+)[\(](([A-Za-z0-9\[\]]*[ ][A-Za-z0-9_]*[, ]*)*)",stri)
        for grp in r1:
                arg = grp[2].split(" ")
                all_arg = grp[1]+'('
                
                for i in range(len(arg)):
                        if(i%2 == 0 and arg[i]!=""):
                                all_arg += arg[i]+', '
                if(len(all_arg) > 1):
                        #read_f.write(all_arg[:-2]+')\n')
                        print (web3.Web3.toHex(web3.Web3.sha3(text = all_arg[:-2]+')')),)
                else:
                        #read_f.write(all_arg+')\n')
                        print (web3.Web3.toHex(web3.Web3.sha3(text = all_arg+')')))
        read_f.close()


def begin(dir_add):
        for filename in os.listdir(dir_add):
                if filename.endswith('.sol'):
                        find_func(root+'/'+filename)
        else:
                begin(dir_add + '/'+ filename)


if __name__ == "__main__":   #If function is called directly thorugh terminal execute begin()
        begin(root)