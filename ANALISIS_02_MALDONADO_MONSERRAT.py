import csv

lista_datos = []
with open("synergy_logistics_database.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    
    for registro in lector:
        lista_datos.append(registro)
        



#OPCIÓN 2 --> Medio de Transporte Utilizado, ¿Cuáles son los 3 medios de transporte más importantes para Synergy logistics considerando el valor de las importaciones y exportaciones? ¿Cuál es medio de transporte que podrían reducir?

print("\n \n \n .::PROPUESTA 2::. \n \n \n")

lista_calc=[]
lista_m=[]
for i in lista_datos:
  if i["transport_mode"] not in lista_m:
    lista_m.append(i["transport_mode"])

totalv,importe,importe_v_prom=0,0,0
for reg in lista_m:
 
 for registro in lista_datos:
   if registro["transport_mode"]==reg:
     totalv+=1
     importe=importe+int(registro["total_value"])
     importe_v_prom=importe/totalv
 lista_calc.append([reg,totalv,importe,importe_v_prom])
 totalv,importe,importe_v_prom=0,0,0

lista_calc.sort(reverse = True, key = lambda x:x[3])
print(lista_calc)

#Opción 3) Valor total de importaciones y exportaciones. Si Synergy Logistics quisiera enfocarse en los países que le generan el 80% del valor de las exportaciones e importaciones ¿en qué grupo de países debería enfocar sus esfuerzos?

def pareto_paises (direccion):
    importe,total,relativo,acumulado=0,0,0,0
    pais_catalogo = []
    pais_pareto = []
    pais_sentido=[]
    for i in lista_datos:
      if direccion==i["direction"]:
        total=total+int(i["total_value"])
        pais_sentido.append(i)
        if i["origin"] not in pais_catalogo:
          pais_catalogo.append(i["origin"])
    for opcion in pais_catalogo:
     for registro in pais_sentido:
       if opcion==registro["origin"]:
        importe=importe+int(registro["total_value"])
     relativo=importe*100/total
     pais_pareto.append([opcion,importe,relativo])
     importe=0
    pais_pareto.sort(reverse = True, key = lambda x:x[1])
    pais_pareto[0].append(pais_pareto[0][2])
    for p in range(0,len(pais_pareto)-1):
     pais_pareto[p+1].append(pais_pareto[p][3]+pais_pareto[p+1][2])
    print ("\n \nPARETO "+direccion+" ORIGIN \n \n "+ str(pais_pareto)+ "\n \n")

print("\n \n \n .::PROPUESTA 3::. \n \n \n")
pareto_paises("Exports")
pareto_paises("Imports")










#OPCIÓN 1 --> 10 rutas más demandadas

def rutas_exportacion_importacion (direccion):
    totalv,importe,importe_v_prom=0,0,0
    rutas_contadas = []
    rutas_conteo = []
    rutas_sentido=[]
      
    for ruta in lista_datos:
     ruta_sentido_actual = [ruta["origin"], ruta["destination"],ruta["direction"]]
     
     if ruta_sentido_actual not in rutas_contadas:
       rutas_contadas.append(ruta_sentido_actual)

       for ruta_bd in lista_datos:

         if ruta_sentido_actual == [ruta_bd["origin"], ruta_bd["destination"],ruta_bd["direction"]]:
           totalv+=1
           importe=importe+int(ruta["total_value"])
           importe_v_prom=importe/totalv
           
       rutas_conteo.append([ruta["origin"], ruta["destination"],ruta["direction"],totalv,importe,importe_v_prom])
       totalv,importe,importe_v_prom = 0,0,0
           
    rutas_conteo.sort(reverse = True, key = lambda x:x[5])

    for r in rutas_conteo:
      if r[2]==direccion:
        rutas_sentido.append(r)
    print ("\n \nTOP 10 MORE DEMANDED "+direccion+" ROUTES \n \n "+ str(rutas_sentido)+ "\n \n")

    
    


                    
print("\n \n \n .::PROPUESTA 1::. \n \n \n")
rutas_exportacion_importacion("Exports")
rutas_exportacion_importacion("Imports")

lista_r,lista_a,lista_h,v,lista_final,c,prom=[],[],[],0,[],0,0
for ruta in lista_datos:
    if ruta["origin"]+ruta["destination"] not in lista_r:
     lista_r.append(ruta["origin"]+ruta["destination"])
    if ruta["year"] not in lista_a:
     lista_a.append(ruta["year"])


for ruta in lista_r:
  print(ruta)
  lista_final.append(ruta)
  for year in lista_a:
    print(year)
    lista_final.append(year)
    v=0
    c=0
    for registro in lista_datos:
      
      if str(registro["origin"])+str(registro["destination"])+str(registro["year"])==str(ruta)+str(year):
        v=v+int(registro["total_value"])
        c+=1

    if v==0:
      print(0)
      prom=0
      lista_final.append(prom)
    else:
      print (v/c)
      prom=v/c
      lista_final.append(prom)
    lista_h.append(str(year)+":"+str(prom))
  lista_final.append([ruta,lista_h])
print(lista_final)



  

