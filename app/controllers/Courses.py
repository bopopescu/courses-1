from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
    def index(self):
        course = self.models['Course'].get_all_courses()
        return self.load_view('index.html', course=course)

    def add(self):
        course_details = {
            'title' : request.form['title'],
            'description' : request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect('/')
    def destroy(self, id):
        destroy = self.models['Course'].get_course_by_id(id)
        return self.load_view('destroy.html', destroy=destroy)
    def delete(self, id):
        self.models['Course'].delete(id)
        return redirect('/')
