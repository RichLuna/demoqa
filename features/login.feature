Feature: Login page

  Scenario: Successful login
     Given we visit login page
     When we enter an username "python" and a password "PythonRules4Life"
     Then we are redirected to the main page

  Scenario Outline: Failed login using wrong credentials and verify error messages
     Given we visit login page
     When we enter an username "<user>" and a password "<pass>"
     Then we receive an error message "<error>"
     
     Examples: Errors
     | user          | pass             | error                                                           |
     | python        | incorrecto       | The password you entered for the username python is incorrect   |
     | nonexistent   | PythonRules4Life | Invalid username                                                |
     | nonexistent   | wrongpassword    | Invalid username                                                |
     | python        | N/A              | The password field is empty                                     |
     | N/A           | PythonRules4Life | The username field is empty                                     |
     | N/A           | N/A              | Please enter your username and password                         |
