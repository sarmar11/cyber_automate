Feature: SQLi through url

Background:
  Given the user logs into PortSwigger

  @security
  Scenario: Force SQLi through url
   Given I open SQLi laboratory
    When add a filter to url "filter?category=any'+OR+1=1--"
    Then I check visible data contains allowed values
