""" 2941 : 크로아티아 알파벳 """

# 크로아티아 알파벳에는 [ c= , c- , dz= , d- , lj , nj , s= , z= ] 있음
# 위 알파벳 1로 카운트해서 주어진 문장이 총 몇 글자로 이루어져있는지 출력

""" my solution """
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st = input()
for a in arr:
    st = st.replace(a, '0')
print(len(st))
