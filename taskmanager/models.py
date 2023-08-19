from taskmanager import db

class Category(db.Model):
    id= db.column(db.Integer, primary_key=True)
    category_name = db.column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category",
     cascade="all,delete",lazy=True)

    def __repr__(self):
        #__repr__ to represent it self inform of a string

        return self.category_name

class Task(db.Model):

    id = db.column(db.Integer, primary_key=True)
    task_name= db.column(db.String(50), unique = True, nullable = False)
    task_description = db.column(db.Text, nullable=False)
    is_urgent= db.column(db.Boolean, default = False, nullable=False)
    due_date = DB.column(db.Date, nullable=Fale)
    category_id= db.column(db.Integer, db.foreignkey("category.id"),
     ondelete="CASCADE", nullable=False)

    def __repr__(self):
       # __repr__ to represent it self in a form of a string

       return "{0}- Task:{1} | urgent :{2}".format(self.id, self.task_name,
        self.is_urgent)
