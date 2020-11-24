# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:51:10 2020

@author: aleks1212
"""

'''
Запись римских цифр. Правила
1. Не ставят больше 3-х одинаковых цифр подряд;
2. Если младшая цифра стоит слева от старшей, то она вычитается.
Иначе цифры складываются.
3. Вычитаться могут только цифры, обозначающие 1 или ступени 10.
4. В качестве уменьшаемого могут выбираться только ближайшие в числовом
ряду к вычитаемой 2 цифры (т.е. вычитаемое, умноженное на 5 или на 10 (вики))
'''

rim_decryption = {
                 'I':1, 
                 'V':5, 
                 'X':10, 
                 'L':50, 
                 'C':100,
                 'D':500,
                 'M':1000
                 }

class Solution:
     
     def isCorrect(self, s: str) -> (bool, str):
        return_str = 'Корректная римская запись числа'
        temp_s = s + ''
        for key in rim_decryption.keys():
            temp_s = temp_s.replace(key, '')
        if temp_s != '':
            return False, 'Неверный формат данных!'
        
        if len(s) > 15 or len(s) == 0:
            return False, 'Неверная длина'
        
        for key in rim_decryption.keys():
            key *= 4
            if key in s:
                return False, 'Четыре или более одинаковых цифр подряд!'
        
        for w1, w2 in zip(s, s[1:]):
            if rim_decryption[w1] < rim_decryption[w2]:
                if str(rim_decryption[w1])[0] != '1':
                    return False, 'Число в неверном формате: вычитаться может только 1 или ступени 10'
                if rim_decryption[w2] / rim_decryption[w1] > 10:
                    return_str = 'Римское число записано в современной упрощенной форме.'
        return True, return_str 

     def romanToInt(self, s: str) -> int:
        deductible = list() #помечаем вычитаемые
        flag = False
        for w1, w2 in zip(s, s[1:]):
            if flag:
                deductible.append(False) #уменьшаемое нельзя вычитать
                flag = False
                continue 
            if rim_decryption[w1] < rim_decryption[w2]:
                deductible.append(True)
                flag = True
            else:
                deductible.append(False)
                flag = False
        deductible.append(False) #последняя цифра не может быть вычитаемым
        
        arab = list()
        for w in s:
            arab.append(rim_decryption[w])
        
        for i, sub in enumerate(deductible):
            if sub:
                arab[i+1] -= arab[i]
                arab[i] = 0
        
        summ = 0        
        for a in arab:
            summ += a
        return summ
        
        
if __name__ == '__main__':        
    test_s = [
            'XVL',
            'XVIII',
            'XIIV',
            'DM',
            'VX',
            'ID'
            'DCCC',
            'XIIII',
            'VI',
            'YGXXX',
            'MCMXCIV',
            'LVIII',
            'IX',
            'IV',
            'III',
            'hello Hapoleon IT!'
            ]
    solution = Solution()
    for test in test_s:
        f, message = solution.isCorrect(test)
        if f:
            print(test, '- арабская запись:', solution.romanToInt(test))
        else:
            print(test, '-', message)