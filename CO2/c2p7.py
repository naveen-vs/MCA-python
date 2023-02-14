'''st=input('enter a word :')
s='ing'
for i in range(0,len(st)):
    if st[-3]=='i' and st[-2]=='n' and st[-1]=='g':
        print(st+'ly')
        break;
    else:
        print(st+'ing')
        break;'''
st=input('enter a word :')
if st.endswith('ing'):
    st += 'ly'
elif len(st)>=3:
    st +='ing'
print(st)