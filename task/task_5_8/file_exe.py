from task.task_5_8.example import Student, Course, Teacher


# 打印标题
def introduction(str):
    print("{}{}{}".format("*" * 20, str, "*" * 20))


# 课程信息初始化方法，返回实例对象的列表
def prepare_course():
    course_dict = {
        "01": "网络爬虫", "02": "数据分析",
        "03": "人工智能", "04": "机器学习",
        "05": "云计算", "06": "大数据",
        "07": "图像识别", "08": "Web开发"
    }
    course_list = []
    for k, v in course_dict.items():
        cour = Course(k, v)
        course_list.append(cour)
    return course_list


# 课程信息绑定老师初始化方法， 返回实例对象的列表
def create_teacher():
    teacher_info_list = [
        ["T1", "张亮", "13301122001"],
        ["T2", "王朋", "13301122002"],
        ["T3", "李旭", "13301122003"],
        ["T4", "黄国发", "13301122004"],
        ["T5", "周勤", "13301122005"],
        ["T6", "谢富顺", "13301122006"],
        ["T7", "贾教师", "13301122007"],
        ["T8", "杨教师", "13301122008"]
    ]
    t_list = []
    for i in teacher_info_list:
        teacher_info = Teacher(*i)
        t_list.append(teacher_info)
    return t_list


# 课程信息绑定老师信息方法，返回字典列表
def course_to_teacher():
    course_info = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for i in range(len(ls_course)):
        # prepare_course 方法返回的是Course实例对象列表，所以在这里可以通过得到的对象调用binding方法
        dic = ls_course[i].binding(ls_teacher[7 - i])
        course_info.append(dic)
    # 返回包含课程绑定教师字典的列表
    return course_info


# 学生信息初始化方法
def create_student():
    ls_student = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    num_list = range(1000, 1008)
    student_list = []
    for i in range(len(ls_student)):
        stu = Student(num_list[i], ls_student[7 - i])
        student_list.append(stu)
    return student_list


if __name__ == "__main__":
    binding = course_to_teacher()
    s_create = create_student()
    # print(s_create)
    introduction("慕课学院（1）班学生信息")
    for i in s_create:
        print(i)

    introduction("慕课学院（1）班选课结果")
    for i in range(len(binding)):
        s_create[i].add_course(binding[i])

    for i in range(len(s_create)):
        # 最好使用对象方法来输出选课信息,属性经过属性方法的返回之后具有一定的安全性.(调用对象方法)
        # print("Name:{}, Selected:{}".format(s_create[i].s_name, s_create[i].course_detail))
        print("Name:{}, Selected:{}".format(s_create[i].s_name, s_create[i].course))
