*** Settings ***
Library     OperatingSystem


*** Test Cases ***
CheckFileExist
    File Should Exist   output.txt

