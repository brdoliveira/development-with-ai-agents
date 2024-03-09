from textwrap import dedent
from crewai import Task

class ProjectTasks:
    def backend_structure_task(self,agent,request):
        return Task(
            description=dedent(f"""\
                Outline the structure for the Kotlin-based backend using the Spring framework,
                including essential components and modules.
                Specific project request: '{request}'
            """),
            agent_in_charge=agent
        )

    def frontend_structure_task(self,agent,request):
        return Task(
            description=dedent(f"""\
                Define the Angular-based frontend structure, focusing on TypeScript and SASS development, utilizing PrimeFaces for UI components.
                Specific project request: '{request}'
            """),
            agent_in_charge=agent
        )

    def backend_development_task(self,agent):
        return Task(
            description="Develop the backend structure using Spring and Kotlin, ensuring scalability and efficiency.",
            agent_in_charge=agent
        )
    
    def frontend_development_task(self,agent):
        return Task(
            description="Design and implement the UI using Angular, TypeScript, SASS, and PrimeNG, focusing on user experience.",
            agent_in_charge=agent
        )

    def ui_implementation_task(self,agent):
        return Task(
            description="Design and implement the UI using Angular, TypeScript, SASS, and PrimeNG, focusing on user experience.",
            agent_in_charge=agent
        )

    def testing_plan_task(self,agent):
        return Task(
            description="Develop detailed unit and integration testing plans, specifying test cases, acceptance criteria, and testing approach, to ensure comprehensive system validation.",
            agent_in_charge=agent
        )

    def backend_unit_tests_task(self,agent):
        return Task(
            description="Develop unit tests for each component of the Kotlin Spring backend, using testing frameworks like JUnit and MockK to ensure reliability and bug-free operation.",
            agent_in_charge=agent
        )

    def frontend_integration_tests_task(self,agent):
        return Task(
            description="Design, develop, and execute integration tests for the frontend using Robot Framework, covering various user scenarios and ensuring cross-browser compatibility.",
            agent_in_charge=agent
        )

    def class_documentation_task(self,agent):
        return Task(
            description="Review and document all classes in the Kotlin project, including descriptions, methods, properties, and relevant notes.",
            agent_in_charge=agent
        )

    def method_documentation_task(self,agent):
        return Task(
            description="Document each method in Kotlin classes, detailing parameters, return value, exceptions thrown, and usage examples.",
            agent_in_charge=agent
        )