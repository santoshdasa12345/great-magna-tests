#Removed show me around
#@show-me-around-page
#@allure.suite:Great_Magna_Show_Me_Around
#Feature:GreatMagna - Show_Me_Around Page
#
#   @allure.link:XOT-011
#   @Great-Magna-Show-Me-Around
#Scenario Outline:Visitor should be able visit page tour
#
#  Given "Robert" visited "GreatMagna - Login" page
#  When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
#  And "Robert" decides to page tour and click "Show me around"
#  And "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#      | email address | password |
#      | santoshtesting10008+888@gmail.com | Testing@123! |