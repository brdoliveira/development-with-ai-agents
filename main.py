from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import ProjectTasks
from agents import DevelopmentAgents

with open('./request.txt', 'r') as file:
    request = file.read()

# Initialize Project Tasks and Development Agents
tasks = ProjectTasks()
agents = DevelopmentAgents()

# Create Agents
arch_web_dev = agents.arch_web_dev()
backend_specialist = agents.backend_specialist()
frontend_specialist = agents.frontend_specialist()
testing_strategy_specialist = agents.testing_strategy_specialist()
development_of_unit_tests_for_kotlin_spring = agents.development_of_unit_tests_for_kotlin_spring()
qa_specialist_robot_framework = agents.qa_specialist_robot_framework()
docu_kotlin = agents.docu_kotlin()

# Create Tasks
backend_structure_task = tasks.backend_structure_task(arch_web_dev,request)
frontend_structure_task = tasks.frontend_structure_task(arch_web_dev,request)

backend_development_task = tasks.backend_development_task(backend_specialist)
frontend_development_task = tasks.frontend_development_task(frontend_specialist)

testing_plan_task = tasks.testing_plan_task(testing_strategy_specialist)
backend_unit_tests_task = tasks.backend_unit_tests_task(development_of_unit_tests_for_kotlin_spring)
frontend_integration_tests_task = tasks.frontend_integration_tests_task(qa_specialist_robot_framework)
method_documentation_task = tasks.method_documentation_task(docu_kotlin)

# Backend Crew
backend_crew = Crew(
	agents=[
		arch_web_dev,
        backend_specialist,
        testing_strategy_specialist,
        development_of_unit_tests_for_kotlin_spring,
        docu_kotlin
	],
	tasks=[
        backend_structure_task,
        backend_development_task,
        testing_plan_task,
        backend_unit_tests_task,
        method_documentation_task
    ],
	verbose=True
)

# Frontend Crew
frontend_crew = Crew(
	agents=[
		arch_web_dev,
        frontend_specialist,
        testing_strategy_specialist,
        qa_specialist_robot_framework
	],
	tasks=[
        frontend_structure_task,
        frontend_development_task,
        testing_plan_task,
        frontend_integration_tests_task
    ],
	verbose=True
)

# Start
backend_result = backend_crew.kickoff()
frontend_result = frontend_crew.kickoff()