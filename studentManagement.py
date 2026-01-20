from leiceshi import student
class studentmanagement:
    def __init__(self):
        self.students=[]
    def add_student(self,name,age,grad):
        new_student=student(name,age,grad)
        self.students.append(new_student)
        print(f"学生:{name}添加成功")
    def found_student(self, name):
        for a in self.students:
            if a.name == name:
                print("yes,we found it")
                return
        print("sorry, we not found, try again")
    def delete_student(self,name):
        for b in self.studentts:
            if b.name==name:
                c=self.student.remove(b)
                print("now,student has already been deleted")
            else:
                print("soryy,we not found,try again")