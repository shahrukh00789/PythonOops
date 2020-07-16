import re

mystring =''' Tata Group  is an Indian multinational conglomerate
 holding company headquartered in Mumbai, Maharashtra, India. Founded in 1868
  by Jamsetji Tata, the company gained international recognition after purchasing several global companies. One of
   India's largest conglomerates, Tata Group
 is owned by Tata Sons.[3][4] It is one of the biggest industrial groups in the country, 
 founded 153 years back in 1868'''

# findall,search,split,sub,finditer
# patt = re.compile(r'.Ta')
patt = re.compile(r'^ Ta')
# patt= re.compile(r'$')
matches=patt.finditer(mystring)

for match in matches:
    print(match)
    # print(mystring[411:415])