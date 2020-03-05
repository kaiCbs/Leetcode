class Solution:
    def removeComments(self, source: List[str], flag = 0) -> List[str]:
        def foo(source: List[str], flag = 0):
            if not source:
                return ""
            line = source[0]
            if flag:
                if "*/" not in line:
                    return foo(source[1:],1)
                else:
                    return foo([line[line.find('*/')+2:]] + source[1:],0)
            else:
                if "/*" in line or "//" in line:
                    a = line.find('/*')
                    b = line.find('//')
                    if (a<b and a!=-1) or b==-1:
                        return line[:a]+foo([line[a+2:]]+source[1:],1)
                    else:
                        return line[:b]+"\n"+foo(source[1:],0)
                else:
                    return line + "\n" + foo(source[1:],0)
        return [i for i in foo(source, 0).split('\n') if i] 

    # def removeComments(self, source):
    #     return filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n'))
    # @StefanPochmann
