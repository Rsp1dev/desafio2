from .models import Tarea, SubTarea

def recupera_tareas_y_subtareas():
    tareas = Tarea.objects.all()
    #print(tareas)

    totales = []
    for item in tareas:
        sub_tareas = item.subtarea.all()
        
        datos = {
            'tarea':item,
            'sub_tareas':sub_tareas
        }
        totales.append(datos)

    return totales

def crear_nueva_tarea(descripcion=''):
    tarea = Tarea(descripcion=descripcion, eliminada=False)
    tarea.save()
    return recupera_tareas_y_subtareas()

def crear_sub_tarea(tarea_asociada_id,descripcion):
    tarea = Tarea.objects.get(id=tarea_asociada_id)
    # tarea = Tarea.objects.filter(id=tarea_asociada_id).first()
    #print(tarea)
    sub_tarea = SubTarea(descripcion=descripcion,eliminada=False, tarea_id=tarea)
    sub_tarea.save()
    return recupera_tareas_y_subtareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_subtareas()

def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_subtareas()

# #def matar_tarea(idtarea:int):
#      t = Tarea.objects.get(id=idtarea) 
#      t.delete()

def imprimir_en_pantalla():
    datos = recupera_tareas_y_subtareas()

    for item in datos:
        print(f"[{item['tarea'].id}] descripción {item['tarea'].descripcion}")

        for st in item['sub_tareas']:
            print(f".... [{st.id}] {st.descripcion}")

    