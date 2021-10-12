@invest
@hpo_pdfs
@pdf
@stage-only
@allure.suite:Invest
Feature: Invest - HPO PDFs sent after

  Background:
    Given test authentication is done


  @allure.link:TT-444
  @dev-only
  @captcha
  Scenario Outline: Check PDFs listed on "Thank you for your enquiry" page for "<selected>" HPO
    Given "Peter Alder" got in touch with us via "Invest - <selected> - Contact us" page
      | field                             | value     |
#      | High productivity food production | checked   |
      | Lightweight        | unchecked |
      | Rail            | unchecked |
    And "Peter Alder" is on the "Invest - Thank you for your enquiry - Contact us" page

    When "Peter Alder" downloads all visible PDFs

    Then "Peter Alder" should see correct details in every downloaded PDF
      | telephone number = +44(0) 207 000 9012    |
      | email address = enquiries@invest-trade.uk |
    And there should not be any dead links in every downloaded PDF

    Examples:
      | selected                          |
      | High productivity food production |


  @allure.link:TT-444
  @dev-only
  @captcha
  Scenario Outline: Check PDFs listed on "Thank you for your enquiry" page for "<selected>" HPO
    Given "Peter Alder" got in touch with us via "Invest - <selected> - Contact us" page
      | field                             | value     |
#      | High productivity food production | unchecked |
      | Lightweight          | checked   |
      | Rail            | unchecked |
    And "Peter Alder" is on the "Invest - Thank you for your enquiry - Contact us" page

    When "Peter Alder" downloads all visible PDFs

    Then "Peter Alder" should see correct details in every downloaded PDF
      | telephone number = +44(0) 207 000 9012    |
      | email address = enquiries@ukti.gsi.gov.uk |
    And there should not be any dead links in every downloaded PDF

    Examples:
      | selected               |
      | Lightweight  |


  @allure.link:TT-444
  @dev-only
  @captcha
  Scenario Outline: Check PDFs listed on "Thank you for your enquiry" page for "<selected>" HPO
    Given "Peter Alder" got in touch with us via "Invest - <selected> - Contact us" page
      | field                             | value     |
#      | High productivity food production | unchecked |
      | Lightweight           | unchecked |
      | Rail              | checked   |
    And "Peter Alder" is on the "Invest - Thank you for your enquiry - Contact us" page

    When "Peter Alder" downloads all visible PDFs

    Then "Peter Alder" should see correct details in every downloaded PDF
      | telephone number = +44(0) 207 000 9012    |
      | email address = enquiries@invest-trade.uk |
    And there should not be any dead links in every downloaded PDF

    Examples:
      | selected            |
      | Rail  |
