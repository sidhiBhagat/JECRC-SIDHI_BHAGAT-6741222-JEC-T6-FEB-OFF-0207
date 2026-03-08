import time

class TODO:
    todos = [
        # {
        #     'id': '',
        #     'desc':'',
        #     'is_completed': False,
        # },{},{},{}
    ]
    
    def add_todo(self, desc):
        ##1. Take the desc from the user.
        
        ##2. we have to create one dictionary in which we will add the todo desc.
        todo_dict={
            'id': int(time.time()),
            'desc': desc,
            'is_completed': False,
        }
        ##3. We have to append that dictionary inside todos list.
        self.todos.append(todo_dict)
    
    def remove_todo(self, id):
        i=0
        while (i<len(self.todos)):
            if self.todos[i]['id'] == id:
                self.todos.pop(i)
                break
            i+=1
    
    def display_todos(self):
        if len(self.todos) == 0: return
        for todo in self.todos:
            if todo['is_completed']:
                print(f" {todo['id']}: {todo['desc']} - Completed")
            else:
                print(f"{todo['id']}: {todo['desc']} - Pending")

    def update_todo(self, id, new_desc):
        for todo in self.todos:
            if todo['id'] == id:
                todo['desc'] = new_desc
    
    def toggle_mark_as_completed(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                todo['is_completed'] = not todo['is_completed']
    
    def completed_todos(self):
        if len(self.todos) == 0: return

        for todo in self.todos:
            if todo['is_completed']:
                print(f"todo {todo['id']}: {todo['desc']} - Completed")
    
    def incompleted_todos(self):
        if len(self.todos) == 0: return

        for todo in self.todos:
            if not todo['is_completed']:
                print(f"todo {todo['id']}:  {todo['desc']} - Pending")


obj=TODO()
# obj.add_todo("learn python")
obj.display_todos()


