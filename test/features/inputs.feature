Feature: XSS through inputs

Background:
  Given the user logs into PortSwigger

  @security
  Scenario Outline: Force XSS through input
   Given I open XSS laboratory
    When I search the value "<value>"
    Then there are no alerts in browser

    Examples:
      | value                               |
      | <script>alert('Crash WEB')</script> |

  Scenario Outline: Check valid values in input
   Given I open XSS laboratory
    When I search the value "<value>"
    Then the filtered elements contain "<value>" value

    Examples:
      | value  |
      | dating |

