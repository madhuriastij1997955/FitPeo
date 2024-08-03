Feature: Login Functionality
  @T1
  Scenario: Login to application with valid username and password
    Given launch the browser and navigate to home page
    When Login to Application with valid username and password
    And click on login button
    Then I should get logged in


#  Scenario: Login to application with invalid username and valid password
#    Given launch the browser and navigate to home page
#    When Enter valid Invalid username and valid password
#    And click on login button    Then Verify proper message is displayed for login page
#
#
#  Scenario: Login to application with valid username and Invalid password
#    Given launch the browser and navigate to home page
#    When Enter valid username and Invalid password
#    And click on login button
#    Then Verify proper message is displayed for login page
#
#
#  Scenario: Login to without entering parameters
#    Given launch the browser and navigate to home page
#    When Don't enter username and passowrd
#    And click on login button
#    Then Verify proper message is displayed for login page


