frontend_skills = {"HTML", "CSS", "JavaScript", "React"} 
backend_skills = {"Python", "JavaScript", "SQL", "React"}

union_set = frontend_skills | backend_skills
# union_set = frontend_skills.union(backend_skills)
print("Union of two set: ", union_set, "\n")

intersection_set = frontend_skills & backend_skills
# intersection_set = frontend_skills.intersection(backend_skills)
print("Intersection of two sets: ", intersection_set, "\n")

difference_set = frontend_skills - backend_skills
# difference_set = frontend_skills.difference(backend_skills)
print("frontend-only difference set: ", difference_set, "\n")

symmetric_difference_set = frontend_skills ^ backend_skills
# symmetric_difference_set = frontend_skills.symmetric_difference(backend_skills)
print("symmetric difference set: ", symmetric_difference_set, "\n")
