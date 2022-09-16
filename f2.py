# int: integer - egész számot jelent
# kor_mint_str:str = input('hány éves vagy? ')
# kor_mint_int:int = int(kor_mint_str)

kor:int = int(input('hány éves vagy? '))


if kor >= 18:
    print('akkor tudsz venni cigit már a dohiboltba')
else:
    print('akkor még fiatalkorú vagy, be sem mehetsz a dohiboltba')