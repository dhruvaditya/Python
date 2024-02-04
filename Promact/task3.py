class Task:
    #Created a class named Task
    def __init__(self, title, description="", status="incomplete"):
        #Attributes are given as per the instruction
        #As mentioned initially we have to make the status as incomplete
        self.title = title
        self.description = description
        # Here we are inputing status as incomplete by just assining the status to self pointer
        self.status = status

    #Here the method is created  in the task class to mark a task as complete
    def mark_as_complete(self):
        self.status = "complete"

    def to_s(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n"
# Encapsulation:Attributes in classes are encapsulated within the classes.

class TaskList:
    #Created a task list that represent a collection of task
    def __init__(self):
        self.tasks = []
    #Implemented methods in the TaskList class to add tasks, remove tasks, list all tasks, and find tasks by title.
    def add_task(self, task):
        self.tasks.append(task)

    def add_task_overload(self, title, description=""):
        task = Task(title, description)
        self.add_task(task)

    def add_priority_task(self, title, description="", status="incomplete", priority="high"):
        task = PriorityTask(title, description, status, priority)
        self.tasks.append(task)
    def remove_task(self, task):
        self.tasks.remove(task)

    def list_all_tasks(self):
        for task in self.tasks:
            print(task.to_s())

    def find_priority_task(self, title):
        for task in self.tasks:
            if isinstance(task, PriorityTask) and task.title == title:
                return task
        return None

    def find_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    #Methods :__init__ constructors for initializing objects


#Implemented inheritance PriorityTask class that inherits from Task
class PriorityTask(Task):
    #Here added additional priority attribute as low
    def __init__(self, title, description="", status="incomplete", priority="low"):
        super().__init__(title, description, status)
        self.priority = priority
    #Used method overriding to customize the to_s method in the Task class to display task details in a user-friendly format.
    #Method Overriding
    def to_s(self):
        return f"{super().to_s()}Priority: {self.priority}\n"
    #to_s :- customized string representation for each display

# Polymorphism: to_s method is polymorphic, providing different implementations in Task and PriorityTask.

# Sample usage of our Task List Application

if __name__ == "__main__":
    #Creating task by object oriented technique
    #Here i am implementing two ways one by doing it manually and other by taking input from user
    #Firstly i have done and understood the concept by giving input my self

    task1 = Task("Do Homework")
    task2 = Task("Go to the gym", "Cardio workout")

    task_list = TaskList()
    task_list.add_task(task1)


    # task_list.add_task_overload("Cardio Workout 2")

    task_list.list_all_tasks()


    print("\nMarking the second task as complete:")
    # Here marking go to Gym as complete by calling the method
    task2.mark_as_complete()
    print(task2.to_s())
    #Adding to the priority_task list
    task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")
    print("\nFinding task by title 'Do Homework':")
    found_task = task_list.find_task_by_title("Do Homework")
    #Checking whether it is present or not by if else if found then print other wise print Task not found
    if found_task:
        print(found_task.to_s())
    else:
        print("Task not found.")
    #Storing boolean in found_priority_task if found then print title, description, status and priority
    found_priority_task = task_list.find_priority_task("Buy groceries")
    if found_priority_task:
        print(found_priority_task.to_s())

# Classes and Objects:
# Classes: Task, TaskList, PriorityTask
# Objects: task1, task2, task_list, priority_task

#As per the instruction i have done with the output now making it more userfriendly by add while loop
#We have run the code seperately like either we can run the above part or below part by commenting one of the part.
 # task_list = TaskList()
 #    task_list = TaskList()
 #    while True:
 #        print("\nTask List Application:")
 #        print("1. Add Task")
 #        print("2. Add Priority Task")
 #        print("3. Mark Task as Complete")
 #        print("4. List Tasks")
 #        print("5. Find Task by Title")
 #        print("6. Find Priority Task by Title")
 #        print("7. Exit")
 #
 #        choice = input("Enter your choice (1-7): ")
 #
 #        if choice == "1":
 #            title = input("Enter task title: ")
 #            description = input("Enter task description (optional): ")
 #            task_list.add_task(title)
 #
 #        elif choice == "2":
 #            title = input("Enter priority task title: ")
 #            description = input("Enter priority task description (optional): ")
 #            priority = input("Enter priority (low/medium/high): ")
 #            task_list.add_priority_task(title, description, priority)
 #
 #        elif choice == "3":
 #            title = input("Enter the title of the task to mark as complete: ")
 #            task_list.mark_as_complete(title)
 #
 #        elif choice == "4":
 #            print("\nList of Tasks:")
 #            task_list.list_all_tasks()
 #
 #        elif choice == "5":
 #            title = input("Enter the title of the task to find: ")
 #            found_task = task_list.find_task_by_title(title)
 #            if found_task:
 #                print(found_task.to_s())
 #            else:
 #                print("Task not found.")
 #
 #        elif choice == "6":
 #            title = input("Enter the title of the priority task to find: ")
 #            found_priority_task = task_list.find_priority_task(title)
 #            if found_priority_task:
 #                print(found_priority_task.to_s())
 #            else:
 #                print("Priority Task not found.")
 #
 #        elif choice == "7":
 #            print("Thank You for using this app, Have a great day from Promact!")
 #            break
 #
 #        else:
 #            print("Invalid choice. Please enter a number between 1 and 7.")