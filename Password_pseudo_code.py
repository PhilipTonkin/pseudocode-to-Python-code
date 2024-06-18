stored_pass <- "password"
password <- ""
pass_mismatch <- stored_pass != password

WHILE pass_mismatch
    OUTPUT "Enter your password:"
    password <- USERINPUT
    pass_mismatch <- stored_pass != password
END WHILE

OUTPUT "Access granted"
