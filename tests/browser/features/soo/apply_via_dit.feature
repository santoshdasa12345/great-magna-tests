@domestic
@allure.suite:SOO
Feature: SOO - Apply via DIT

  Background:
    Given test authentication is done


  @allure.link:XOT-689
  @exopps
  @captcha
  @dev-only
  @soo-long-domestic_1
  @account-support
  @read-only
  Scenario Outline: Anonymous Enquirers should be redirected to SSO login page
    Given "Robert" found a marketplace in "<country>" to sell "<products>"

    When "Robert" decides to "Apply now"

    Then "Robert" should be on the "SSO - Sign in" page

    Examples: products and countries
      | country   | products                 |
      | Australia | Clothing and accessories |

