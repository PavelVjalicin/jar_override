# jar_override
Override and add files to jar

# How to use

1. Place a single jar file into input directory.

2. Place java code that you want to add to jar file into code directory. (directory structure should be the same as of jar file)

# Example

Input jar structure:
    org/company/Main.class
    org/otherCompany/Library.class
    org/secondLibrary/Library.class
    MATA-INF/MANIFEST.MF

Code directory structure:
    org/company/Main.java
    org/company/SomeClass.java
    org/otherCompany/Library.java

Output jar structure:
    org/company/Main.class
    org/company/SomeClass.java
    org/otherCompany/Library.class
    org/secondLibrary/Library.class
    MATA-INF/MANIFEST.MF


In this case org/company/Main.class, org/otherCompany/Library.class will be overriden with classes located in code directory.
Additional file will be added since it didn't exist before (org/company/SomeClass.class).