import iFactory.iDB as DB
import iFactory.D_Alive as i1
import iFactory.A_Alive as i2
import iFactory.P_Op as i3
import iFactory.D_Op as i4
import iFactory.Ras_Op as i5
import iFactory.DB_Up as i6
import iFactory.API_i as i7
 
# a = i1.Alive()
# b = i2.Alive()
# c = i3.Operate()
# d = i4.Operate()
# e = i5.Operate()
# f = i6.Update()
# g = i7.API()
# print(a,b,c,d,e,f,g)   

iDB = DB.Get_DB()

ip_list = list()
for p in iDB:
    ip_list.append(list((p.dev_id,p.dev_ip)))
    
import json 
i={}   
i["xxx"] = [1,2,3]
d = json.dumps(i)
print(d)

# i1.Alive(ip_list)    
   
    
# print(ip_list)
