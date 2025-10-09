class TaskManager:
    task:dict[str, dict]
    
    def __init__(self, tasks:dict[str, dict[str|bool]])->None:
        self.setTasks(tasks)
    
    
    
    def setTasks(self, tasks:dict[str, dict[str|bool]]):
        if isinstance(tasks, dict):
            self.task = tasks 
            for key,value in self.task.items():
                if isinstance(key, str) and isinstance(value,dict ):
                    self.task[key] = value
            else:
                raise ValueError(f"Errore! La chiave: {key} deve essere una stringa e il valore: {value} deve essere una stringa")
        else:
            raise ValueError('Errore!')
    
    
    def Tasks(self)-> dict:
        return self.task
    
    
    def create_task(self, task_id:str, descrizione:str)-> dict|str:
        if task_id in self.task:
            return f"Errore! La chiave esiste già"
        else:
            temp_dict:dict[str, dict[str, bool|str]] = {'description': descrizione, 'completato': False}
            self.task[task_id] = temp_dict
            # self.task[task_id] = {'description': descrizione, 'completato': False}
        return temp_dict
    
    
    
    def complete_task(self,task_id:str)-> dict|str:
        if task_id not in self.task:
            return "Chiave non esistente"
        else: 
            if self.task[task_id]["completato"]: 
                return  "Il task è già completato"
            else:
                self.task[task_id]["completato"] = True
            return self.task[task_id] 
        
    
    def update_description(self, task_id:str, nuova_descrizione:str)-> dict|str:
        if task_id not in self.task:
            return "Il task non è nel dizionario"
        
        else: 
            self.task[task_id]['description'] = nuova_descrizione
            return self.task[task_id]
    
    def remove_task(self, task_id:str)->dict|str:
        if task_id not in self.task:
            return "Task non presente"
        else:
            return self.task.pop(task_id)
            
    
    
    
    
    def list_task(self)->list[str]:
        # lista_chiavi: list[str] = list()
        # for key in self.task.keys():
        #     lista_chiavi.append(key)
        # return lista_chiavi
        return [self.task.keys()]
    
    
    def get_task(self, task_id):
        if task_id not in self.task:
            return "Task non presente"
        else:
            return self.task[task_id]




