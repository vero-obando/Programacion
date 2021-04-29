# Encuesta sobre deportes favoritos 
import matplotlib.pyplot as plt
deportes = ['Futbol','Voleibol','Baloncesto','Tenis','Beisbol']
encuesta = [25,30,5,25,15]
plt.bar(deportes,encuesta,color= 'c')
plt.title('Deportes favoritos')
plt.xlabel('Deportes')
plt.ylabel('% de gusto')
plt.show()
