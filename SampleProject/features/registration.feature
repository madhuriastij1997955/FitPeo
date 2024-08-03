Feature: Test the Registartaion functionality

  @Test1
  Scenario: Register with manadtory fields
    Given Launch the browser and navigate to registration page
    When  Enter all manadatory fields
    And Click on continue button
    Then Account should be created




  @Test2
  Scenario: Register with exsiting mailid
    Given Launch the browser and navigate to registration page
    When  Enter all manadatory fields except mailid
    And  Enter exsiting mailid
    And  Click on continue button
    Then Account should not be created and error message should be displayed

  @Test3
  Scenario: Register not providing details
    Given Launch the browser and navigate to registration page
    When  Do not enter values in registartion page
    And  Click on continue button
#    Then Proper warning message should be displayed for all mandatory fields