Feature: Search functionality

  Scenario: Search for valid product
#    Given launch the browser and navigate to home page1
    When Enter valid product in search box
    And Click on search box
    Then Validate product should get displayed in search results



  Scenario: Search for Invalid product
#    Given launch the browser and navigate to home page1
    When Enter Invalid product in search box
    And Click on search box
    Then Validate Proper message is displayed in search results

  @S1
  Scenario: Search product without entering any product
#    Given launch the browser and navigate to home page1
    When Do not search product in search box
    And Click on search box
#    Then Validate Proper message is displayed in search results