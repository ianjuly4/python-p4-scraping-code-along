from Course import Course

class Test_Course:
    '''Course in Course.py'''

    def test_title_instance_variable(self):
        "Test setting and getting for title"
        course = Course(title="Programming Robots for Outer Space", schedule="Full-Time", description="Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover")
        assert(course.title == "Programming Robots for Outer Space", course.schedule == "Full-Time", course.description == "Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover")

    def test_schedule_instance_variable(self):
        "Test setting and getting for schedule"
        course = Course(schedule="Full-Time",title="Programming Robots for Outer Space",description="Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover")
        assert(course.schedule == "Full-Time", course.title == "Programming Robots for Outer Space", course.description == "Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover")

    def test_description_instance_variable(self):
        "Test setting and getting for description"
        course = Course(description="Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover", title="Programming Robots for Outer Space", schedule="Full-Time")
        assert(course.description == "Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover", course.title == "Programming Robots for Outer Space", course.schedule == "Full-Time")
