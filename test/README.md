# Running BDD Tests

## Run all features
`pytest --gherkin-terminal-reporter`

## Run specific feature
`pytest tests/features/auth.feature`

## Generate BDD report
`pytest --gherkin-terminal-reporter --html=report.html`

## Run tests with specific tag
`pytest -k "auth"`

# How to use Tests
1. Acceptance Tests are often the starting point, driven by business scenarios and user stories.
2. Integration Tests and Unit Tests are guided by acceptance tests, ensuring system internals align with desired outcomes.

Unit tests verify internal logic, integration tests ensure coherent behavior across modules, and acceptance tests validate the system from the end user's perspective.

This takes a Behavior Driven Development (BDD) approach to testing.

## Shared Vocabulary
BDD uses human-readable descriptions of software user requirements as the basis for software tests. An early step in BDD is the definition of a shared vocabulary between stakeholders, domain experts, and engineers. This process involves the definition of entities, events, and outputs that the users care about, and giving them names everyone agree on.

That vocabulary is used to create a domain-specific language (DSL) they can use to encode system tests such as User Acceptance Tests (UAT).

Note that this language is focused exclusively on the business value that a customer should get from the software rather than describing the user interface of the software, or how the software should accomplish the goals.

## Designing up front Helps Reduce Rework


# Types of Tests

## Acceptance Tests
Purpose: Validate that the system behaves as expected from the user's perspective, meeting business requirements.
Example: "As a user, I want to be able to log in to the system"
How they are used:
- Written collaboratively by developers, testers, and business stakeholders.
- Often defined in a Gherkin syntax (Given, When, Then).
- Focus on high-level scenarios describing the desired behavior without delving into technical implementation.
- Serve as the foundation for ensuring aligntment between business expectations and technical outcomes.

## Integration Tests
Purpose: Ensure that different parts of the application work together as expected.
Example: Testing how the user authentication service interacts with the database and an email API.
How they are used:
- Written to confirm the behavior of multiple units or components working together.
- Help identify issues with API calls, database queries, or third-party integrations.
- Often written alongside step definitions for acceptance tests, ensuring that the behaviors described in scenarios function across boundaries.

## Unit Tests
Purpose: Verify the behavior of individual components or methods in isolation.
Example: A calculator should return 4 when adding 2 and 2.
How they are used:
- Test the smallets units of the application, focusing on expected behaviors rather than implementation details.

# Tools
This project uses `pytest-bdd` for tests.
