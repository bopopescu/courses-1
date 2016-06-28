from system.core.model import Model
class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, course_id):
        # pass data to the query like so
        query = "SELECT * FROM courses WHERE id = %s"
        data = [course_id]
        return self.db.query_db(query, data)

    def add_course(self, course):
      # Build the query first and then the data that goes in the query
      query = "INSERT INTO courses (title, description, created_at) VALUES (%s, %s, NOW())"
      data = [course['title'], course['description']] # Note that data must be an array
      return self.db.query_db(query, data)

    def update_course(self, course):
      # Building the query for the update
      query = "UPDATE courses SET title=%s, description=%s WHERE id = %s"
      # we need to pass the necessary data
      data = [course['title'], course['description'], course['id']]
      # run the update
      return self.db.query_db(query, data)

    def delete(self, id):
      query = "DELETE FROM courses WHERE id = %s"
      data = [id]
      return self.db.query_db(query, data)