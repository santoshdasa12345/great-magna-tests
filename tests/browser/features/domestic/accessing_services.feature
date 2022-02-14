#@domestic
#@services
#@allure.suite:Domestic
#Feature: Domestic - Accessing Services
#
#  Background:
#    Given test authentication is done


#  @allure.link:ED-2659
#  @home-page
#  @passed
#  @accessing-services_1
#  Scenario: Any Exporter visiting the Services page should be able to see links to all relevant Services
#    When "Robert" goes to the "Domestic - Services" page
#
#    Then "Robert" should see following sections
#      | sections               |
#      | Header                 |
#      | SSO links - logged out |
#      | Breadcrumbs            |
#      | Services               |
#      | Error reporting        |
##      | Footer                 |
#
#
#  @dev-only
#  @allure.link:TT-1120
#  @ltd-plc-royal
#  Scenario Outline: "<business type>" representative should receive an email with confirmation code
#    Given "Natalia" visits the "Profile - Enter your email address and set a password (<business type>)" page
#
#    When "Natalia" fills out and submits the form
#
#    Then "Natalia" should be on the "Profile - Enter your confirmation code (<business type>)" page
#    And "Natalia" should see following sections
#      | sections                     |
#      | Confirmation code message    |
#      | Confirmation code form       |
#      | An option to resend the code |
#      | Enrolment progress bar       |
#    And "Natalia" should receive email confirmation code
#
#    Examples:
#      | business type             |
#      | LTD, PLC or Royal Charter |
#
#  @bug
#  @allure.issue:ED-2702
#  @allure.link:ED-2661
#  @home-page
#  @accessing-services_2
#  @<service>
#  @external-service_1
#  Scenario Outline: Any Exporter should be able to get to the "<specific>" Service page from "Domestic - Services" page
#    Given "Robert" visits the "Domestic - Services" page
#
#    When "Robert" decides to find out more about "<service>"
#
#    Then "Robert" should be on the "<specific>" page
#
#    Examples:
#      | service                   | specific                       |
#      | Create a business profile | Find a Buyer - Home            |
#      | Find online marketplaces  | Selling online overseas - Home |
#      | Find export opportunities | Export Opportunities - Home    |
#      | UK Export Finance         | Domestic - Get Finance         |
#      | Find events and visits    | Events - Home                  |
#      | Get an EORI number        | EORI - Home                    |
#      | Report A Trade Barrier    | Domestic - Report a trade barrier   |
#
