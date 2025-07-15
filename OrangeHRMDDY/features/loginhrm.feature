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
@OrangeHRMLoginFeature
Feature: Orange HRM Login feature

	Background: List of background steps for Login feature
		Given Chrome browser is launched
    When User navigates to OrangeHRM Login page
    
    
  @LOG_TC_001
  Scenario: Validate navigation to OrangeHRM Login page
  
    Then User should able to see auth/login in current page url

  @LOG_TC_002
  Scenario: Validate login to OrangeHRM site
    When User enters username
    And User enters password
    And User clicks on login button
    Then User should able to see dashboard/index in current page url

  @LOG_TC_003
  Scenario: OrangeHRM Login with  parameters
    When User enters username "Admin"
    And User enters password "admin123"
    And User clicks on login button
    Then User should able to see "dashboard/index" in current page url
    
    
  @LOG_TC_004
  Scenario Outline: OrangeHRM Login in DDT
    When User enters username "<username>"
    And User enters password "<password>"
    And User clicks on login button
    Then User should able to see "<expected_url_member>" in current page url

    Examples: 
      | username | password  | expected_url_member |
      | Admin    | admin123  | dashboard/index     |
      | Admins   | admin123  | auth/login          |
      | Admin    | admin234  | auth/login          |
      | Admins   | admin1234 | auth/login          |
