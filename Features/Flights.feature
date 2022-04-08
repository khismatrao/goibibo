Feature: Flight booking test

  Scenario: Flights booking successfully
    Given I Launch chrome browser
    When user display home page
    Then select trip
    Then Enter the source and destination
    Then select dates
    And click on search flights button
    Then user close browser