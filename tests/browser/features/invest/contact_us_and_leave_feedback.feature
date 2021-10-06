@investment_atlas
@contact-us_invest
@allure.suite:Invest
Feature: Invest - Contact us and Leave feedback

  Background:
    Given test authentication is done


  @allure.link:CMS-237
  @contact-us
  @dev-only
  @captcha
  @header
  @footer
  Scenario: An email should be sent after visitor submits the contact-us form
#    Given "Robert" visits the "Invest - landing" page
#    And "Robert" decided to "Get in touch"
#    And "Robert" is on the "Invest - Contact us" page
    Given "Robert" visits the "Invest - contact us" page


    When "Robert" fills out and submits the form

    Then "Robert" should be on the "Invest - Thank you for your message" page
    And an "email" notification entitled "Contact form user email subject" should be sent to "Robert"
    And an email notification about "Robert"'s enquiry should be send to "Invest mailbox"


    @allure.link:TT-758
  @international
  @contact-us_24
  Scenario: International Enquirers should be able to see all expected contact options on the "International - What would you like to know more about?" page
    Given "Robert" visits the "Domestic - Contact us" page

    When "Robert" says that his business is "Outside the UK"

    Then "Robert" should be on the "Domestic - What would you like to know more about? - International Contact us" page
    And "Robert" should see following form choices
      | radio elements              |
      | Expanding to the UK         |
      | Investing capital in the UK |
      | Find a UK business partner  |
      | The transition period       |
      | Other                       |


  @allure.link:TT-758
    @international
    @contact-us_25
    @failed
  Scenario Outline: International Enquirers should be able to get to the "<expected>" form for "<selected>"
    Given "Robert" got to the "Domestic - What would you like to know more about? - International Contact us" page via "Outside the UK"

    When "Robert" chooses "<selected>" option

    Then "Robert" should be on the "<expected>" page

    Examples:
      | selected                    | expected                                                |
      | Expanding to the UK         | Invest - Contact us                                     |
#      | Investing capital in the UK | International - Contact the Capital Investment team     |
#      | Find a UK business partner  | International - Find a UK business partner - Contact us |
#      | The transition period       | International - Transition period enquiries             |
#      | Other                       | International - Contact us                              |

#there is no back link
#  @allure.link:TT-758
#    @going-back
#    @contact-us_26
#    @failed
#  Scenario Outline: Enquirers should be able to navigate back to previous pages from "<path>" back to "<expected>" page
#    Given "Robert" navigates via "<path>"
#
#    When "Robert" decides to use "back" link
#
#    Then "Robert" should be on the "<expected>" page
#
#    Examples:
#      | path                                                                                | expected                                                    |
#      | The UK                                                                              | Domestic - Contact us                                       |
#      | Outside the UK                                                                      | Domestic - Contact us                                       |
#      | The UK -> Great.gov.uk account and services support                                 | Domestic - What can we help you with? - Domestic Contact us |
#      | The UK -> Great.gov.uk account and services support -> Export opportunities service | Domestic - Great.gov.uk account and services support        |
#      | The UK -> Great.gov.uk account and services support -> Your account on Great.gov.uk | Domestic - Great.gov.uk account and services support        |
#

 @allure.link:TT-758
  @international_invest_contactus
  @contact-us_24
  Scenario: International Enquirers should be able to see all expected contact options on the "International - What would you like to know more about?" page
    Given "Robert" visits the "Domestic - Contact us" page

    When "Robert" says that his business is "Outside the UK"

    Then "Robert" should be on the "Domestic - What would you like to know more about? - International Contact us" page
    And "Robert" should see following form choices
      | radio elements              |
      | Expanding to the UK         |
      | Investing capital in the UK |
      | Find a UK business partner  |
      | The transition period       |
      | Other                       |
