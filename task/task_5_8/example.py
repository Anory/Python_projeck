

class Student(object):
    def __init__(self, s_number, s_name):
        """
        编写学生类
        :param s_number: 学号
        :param s_name: 姓名
        """
        self.s_number = s_number
        self.s_name = s_name
        self.course = []

    #
    @property
    def course_detail(self):
        return self.course

    # 添加课程信息
    def add_course(self, cour_info):
        self.course_detail.append(cour_info)

    # 返回类的描述信息（当实例对象调用print方法的时候会自动调用该方法）
    def __str__(self):
        return "name：{}，s_number：{}".format(self.s_name, self.s_number)


class Teacher(object):
    def __init__(self, t_number, t_name, p_number):
        """
        编写教师类
        :param t_number: 教师编号
        :param t_name: 教师姓名
        :param p_number: 教师手机号码
        """
        self.t_number = t_number
        self.t_name = t_name
        self.p_number = p_number

    # 返回教师编号和教师名称属性
    def __str__(self):
        return self.t_number, self.t_name


class Course(object):
    def __init__(self, c_number, c_name, teacher=None):
        """
        编写课程类
        :param c_number: 课程编号
        :param c_name: 课程名字
        :param teacher: 授课老师
        """
        self.c_number = c_number
        self.c_name = c_name
        self.teacher = teacher

    # 课程名称绑定课程老师，返回字典
    def binding(self, teacher):
        if teacher:
            self.teacher = teacher
            c_dict = {"课程名称": self.c_name, "教师名称": self.teacher.t_name}
            return c_dict
        else:
            return None


