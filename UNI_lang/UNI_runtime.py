import sys
import re

class UNI_Lang:
    def __init__(self):
        self.data = [0]*256
    
    def toNumber(self,code):
        tokens = code.split('특대')
        result = 1
        for token in tokens:
            num = (self.data[int(re.sub(r'[^0-9]','',token[:token.find('스윽')]))-4]if token.count('스윽') else 0) + token.count('유') - token.count('니')
            result *= num
        return result
    
    @staticmethod
    def type(code):
        if '#' == code[0]:
            return 'COMMENT'
        if '비질게라고할뻔' in code:
            return 'NOTIF'
        if '비질게' in code:
            return 'IF'
        if '욘서' in code:
            return 'MOVE'
        if '디질게' in code:
            return 'END'
        if '입니다' in code:
            return 'INPUT'
        if '나니고레' in code:
            return 'PRINTUNI'
        if '나니' in code:
            return 'PRINT'
        if '챨' in code:
            return 'DEF'
    def compileLine(self,code):
        if code == '':
            return None
        TYPE = self.type(code)
        if TYPE == 'DEF':
            var, cmd = code.split('챨')
            self.data[int(var)-4] = self.toNumber(cmd)
        elif TYPE == 'END':
            sys.exit()
        elif TYPE == 'INPUT':
            self.data[int(code.replace('챨입니다',''))-4] = int(input())
        elif TYPE == 'PRINT':
            print(self.toNumber(code[2:-1]), end='')
        elif TYPE == "PRINTUNI":
            value = self.toNumber(code[4:-1])
            print(chr(value) if value else '\n', end='')
        elif TYPE == 'IF':
            cond,cmd = code.split('비질게')
            if self.toNumber(cond) == 0:
                return cmd
        elif TYPE == 'NOTIF':
            cond,cmd = code.split('비질게라고할뻔')
            if self.toNumber(cond) != 0:
                return cmd
        elif TYPE == 'MOVE':
            return self.toNumber(code.replace('욘서',''))
        elif TYPE == 'COMMENT':
            pass
    
    def compile(self, code, check=True, errors=100000):
        forgive = False
        recode = ''
        splitter = '\n' if '\n' in code else '!'
        code = code.rstrip().split(splitter)
        if check and (code[0].replace(" ","") != '안녕하시지' or code[-1] != '디비자시지' or not code[0].startswith('안녕하시지')):
            raise SyntaxError('파딱파딱 고쳐야겠지?')
        index = 0
        error = 0
        while index < len(code):
            errorline = index
            c = code[index].strip()
            res = self.compileLine(c)
            if forgive:
                forgive = False
                code[index] = recode
            if isinstance(res, int): #move
                index = res-2
            if isinstance(res, str): #if
                recode = code[index]
                code[index] = res
                index -= 1
                jun = True
            
            index += 1
            error += 1
            if error == errors:
                raise RecursionError(str(errorline+1) + '번째 줄 좀 그만하시지~')
    
    def compilePath(self, path):
        with open(path) as file:
            code = ''.join(file.readlines())
            self.compile(code)
