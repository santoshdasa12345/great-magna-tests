@domestic
@allure.link:TT-1033
@allure.link:TT-1094
@enrol
@new-registration
@allure.suite:Profile
Feature: Profile - CH enrolment flows

  Background:
    Given test authentication is done


  @allure.link:TT-1115
  Scenario: Users should be presented with the Enrolment Steps prior to starting the registration process
    Given "Natalia" visits the "Profile - Create an account" page

    When "Natalia" decides to "start"

    Then "Natalia" should be on the "Profile - Select your business type" page
    And "Natalia" should see following sections
      | sections               |
      | Breadcrumbs            |
      | Form                   |
      | Enrolment progress bar |
    And "Natalia" should see following form choices
      | radio elements                        |
      | LTD, PLC or Royal Charter             |
      | Sole trader or other type of business |
      | UK taxpayer                           |
      | Overseas Company                      |

