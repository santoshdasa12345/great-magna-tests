@domestic
  @invest
@fas-contact-us
  @international
@no-sso-email-verification-required
  @international_2
@allure.suite:International
Feature: FAS - Contact us

  Background:
    Given test authentication is done




  @report-this-page
  @failed
  Scenario Outline: Buyers should be able to get to "Domestic - Feedback" form in order to report a problem with "<specific> Industry" page
    Given "Robert" visits the "International - <specific> - industry" page

#    When "Robert" decides to "report a problem with the page"

#    Then "Robert" should be on the "Domestic - Feedback" page

#    Examples: common industries
#      | specific                            |
#      | Agritech                |

    @full

    Examples: promoted industries
      | specific                            |
      | Carbon capture usage and storage                          |
      | Chemicals                           |
#      | Green finance                           |
      | Greener Buildings      |
      | Hydrogen        |
      | Jet zero and green ships                     |
      | Sustainable infrastructure                         |
#      | Space                               |
#      | Technology                          |

    @full
    @stage-only
    Examples: promoted industries
      | specific                            |
#      | Engineering and manufacturing       |
#      | Financial and professional services |
#      | Legal services                      |
#      | Technology                          |


#  @dev-only
#  @captcha
#   @failed
#    @invest_fix
#  @report-this-page
#  Scenario Outline: Buyers should be able to report a problem with the "<specific>" page
#    Given "Robert" visits the "International - <specific> - industry" page
##    And "Robert" decided to "report a problem with the page"
#    And "Robert" is on the "Domestic - Feedback" page
#
#    When "Robert" fills out and submits the form
#
#    Then "Robert" should be on the "Domestic - Thank you for your feedback" page
#
#    Examples: common industries
#      | specific                            |
#      | Agritech                |
#

