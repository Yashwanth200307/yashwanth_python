#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@tag
Feature: Oange HRM Login Feature

  @tag1
  Scenario: Validate navigate to OrangeHRM Login page
    Given Chrome browser is launched
    When User navugates to OrangeHRM Login page
    Then User should able to see auth/login in current page url
    And check more outcomes
    
    
  Scenario: Validate navigate to OrangeHRM Login page
    Given Chrome browser is launched
    When User navugates to OrangeHRM Login page
    And User enters username
    And User enters Password
    And user click on login button
    Then user should able to see dashboard/index in current page url 
    
  Scenario:    
    

  @tag2
  Scenario Outline: Title of your scenario outline
    Given I want to write a step with <name>
    When I check for the <value> in step
    Then I verify the <status> in step

    Examples: 
      | name  | value | status  |
      | name1 |     5 | success |
      | name2 |     7 | Fail    |
