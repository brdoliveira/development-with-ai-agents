from agents import DevelopmentAgents
from crewai import Task

class ProjectTasks:
    def __init__(self):
        self.agents = DevelopmentAgents()
        
    def backend_structure_task(self):
        return Task(
            description="Outline the structure for the Kotlin-based backend using the Spring framework, including essential components and modules.",
            agent_in_charge=self.agents.arch_web_dev().name
        )

    def frontend_structure_task(self):
        return Task(
            description="Define the Angular-based frontend structure, focusing on TypeScript and SASS development, utilizing PrimeFaces for UI components.",
            agent_in_charge=self.agents.arch_web_dev().name
        )

    def backend_development_task(self):
        return Task(
            description="Develop the backend structure using Spring and Kotlin, ensuring scalability and efficiency.",
            agent_in_charge=self.agents.backend_specialist().name
        )

    def ui_implementation_task(self):
        return Task(
            description="Design and implement the UI using Angular, TypeScript, SASS, and PrimeNG, focusing on user experience.",
            agent_in_charge=self.agents.frontend_specialist().name
        )

    def testing_plan_task(self):
        return Task(
            description="Develop detailed unit and integration testing plans, specifying test cases, acceptance criteria, and testing approach, to ensure comprehensive system validation.",
            agent_in_charge=self.agents.testing_strategy_specialist().name
        )

    def backend_unit_tests_task(self):
        return Task(
            description="Develop unit tests for each component of the Kotlin Spring backend, using testing frameworks like JUnit and MockK to ensure reliability and bug-free operation.",
            agent_in_charge=self.agents.development_of_unit_tests_for_kotlin_spring().name
        )

    def frontend_integration_tests_task(self):
        return Task(
            description="Design, develop, and execute integration tests for the frontend using Robot Framework, covering various user scenarios and ensuring cross-browser compatibility.",
            agent_in_charge=self.agents.qa_specialist_robot_framework().name
        )

    def class_documentation_task(self):
        return Task(
            description="Review and document all classes in the Kotlin project, including descriptions, methods, properties, and relevant notes.",
            agent_in_charge=self.agents.docu_kotlin().name
        )

    def method_documentation_task(self):
        return Task(
            description="Document each method in Kotlin classes, detailing parameters, return value, exceptions thrown, and usage examples.",
            agent_in_charge=self.agents.docu_kotlin().name
        )