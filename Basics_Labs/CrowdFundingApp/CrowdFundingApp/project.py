import json
from utils import validate_date

class Project:
    def __init__(self, title, details, target, start_date, end_date, owner_email):
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.owner_email = owner_email

    def to_dict(self):
        return {
            "title": self.title,
            "details": self.details,
            "target": self.target,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "owner_email": self.owner_email
        }


# the following function is used by later functions to save data
def save_projects(projects):
    try:
        with open('projects_data.json', 'w') as file:
            json.dump(projects, file, indent=4)         # only save projects variable as a json format
        return True
    except Exception as e:
        print(e)
        return False

    # else:               # Executed only if the try condition is true, use "finally" instead if you want to execute this block in all cases even if there was an error
    #     projects.append(project.to_dict())          # "project" here is the user parameter which passed at first and holds new_project object data
        
    #     with open('projects_data.json', 'w') as file:
    #         json.dump(projects, file, indent=4)



def create_project(user_email):
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    target = input("Enter project total target (in EGP): ")
    start_date = validate_date("Enter project start date (YYYY-MM-DD): ")
    end_date = validate_date("Enter project end date (YYYY-MM-DD): ")

    new_project = Project(title, details, target, start_date, end_date, user_email)

    # open the file for read and load data to "projects" variable
    try:
        with open('projects_data.json', 'r') as file:
            projects = json.load(file)
    except Exception as e:
        print(e)
        return False
    
    # append new_project returned data to projects variable
    projects.append(new_project.to_dict())
    
    # save_projects(new_project)
    
    print("Project created successfully!")



def view_all_projects():
    try:
        with open('projects_data.json', 'r') as file:
            projects = json.load(file)
    except Exception as e:
        print(e)
        return False
    
    if not projects:
        print("No projects found.")
    else:
        for project in projects:
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Target: {project['target']} EGP")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print(f"Owner: {project['owner_email']}")
            print("=" * 20)    # print "=" 20 times, means line of equal sign


def edit_project(user_email):
    title_to_edit = input("Enter the title of the project you want to edit: ")
    
    try:
        with open('projects_data.json', 'r') as file:
            projects = json.load(file)
    except FileNotFoundError:
        print("No projects found.")
        return

    project_found = False
    for project in projects:
        if project['title'] == title_to_edit and project['owner_email'] == user_email:     # confirm that project title belongs to the logged email
            project_found = True
            print("Editing project...")
            project['title'] = input("Enter new title: ") or project['title']           # 'or' for the default value to be applied 
            project['details'] = input("Enter new details: ") or project['details']
            project['target'] = input("Enter new target (EGP): ") or project['target']
            project['start_date'] = validate_date("Enter new start date (YYYY-MM-DD): ") or project['start_date']
            project['end_date'] = validate_date("Enter new end date (YYYY-MM-DD): ") or project['end_date']
            break

    if not project_found:
        print("Project not found or you don't have permission to edit this project.")
        return

    if save_projects(projects):
        print("Project updated successfully!")
    else:
        print("Failed to update project.")




def delete_project(user_email):
    title_to_delete = input("Enter the title of the project you want to delete: ")

    try:
        with open('projects_data.json', 'r') as file:
            projects = json.load(file)              # load projects into variable
    except FileNotFoundError:
        print("No projects found.")
        return

    project_found = False           # create bool variable to check on later in this function
    for project in projects:
        if project['title'] == title_to_delete and project['owner_email'] == user_email:
            project_found = True    # set var to True
            projects.remove(project)    # delete project
            break

    if not project_found:
        print("Project not found or you don't have permission to delete this project.")
        return

    if save_projects(projects):
        print("Project deleted successfully!")
    else:
        print("Failed to delete project.")
