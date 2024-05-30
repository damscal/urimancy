1. Requirements Gathering:
    1. Define the scope of the project.
        - solving the problem of maintaining unbreakable references to files and directories. Doing so by separating the concerns of storage (handled by a simple, static hierarchy) and retrieval (handled by a database).
    1. Identify the key stakeholders.
    1. Document the functional and non-functional requirements.

1. System Design:
    1. Design the architecture of the Urimancy system.
    1. Define the structure of the Urimancy Store ‘S’.
    1. Design the mechanism for monitoring changes in the associated directory ‘D’.
    1. Design the mechanism for replacing files/folders in ‘D’ with links ‘L’.
    1. Design the mechanism for handling the deletion of links ‘L’ and files/folders ‘F’.
    1. Design the database schema for storing tags and metadata.

1. Implementation:
    1. Implement the file monitoring service.
    1. Implement the file copying mechanism.
    1. Implement the link creation mechanism.
    1. Implement the deletion mechanisms for ‘L’ and ‘F’.
    1. Implement the database for storing tags and metadata.

1. Testing:
    1. Unit testing: Test individual components to ensure they work as expected.
    1. Integration testing: Test the interaction between different components.
    1. System testing: Test the entire system as a whole.
    1. Acceptance testing: Validate the system against the original requirements.

1. Deployment:
    1. Plan the deployment strategy.
    1. Deploy the system in a controlled environment for further testing.
    1. Once validated, deploy the system in the production environment.

1. Maintenance:
    1. Monitor the system for any issues.
    1. Regularly update the system to handle new requirements or fix bugs.