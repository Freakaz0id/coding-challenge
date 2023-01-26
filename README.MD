A coding challenge using Python and Django

# Tasks #
1. Create a Django project **myproject** and app **core** and two models: **ProcessChain** and **ProcessStep**. A ProcessChain has many related ProcessSteps.
* ProcessStep:
    * Has a field **cost**.
* ProcessChain:
    * Has a field **total_cost**.
    * Has a method **calculate_total_cost**, which sums the cost of all related ProcessSteps and saves it as its total_cost value. If you can, avoid a for-loop in python and use a Django database function instead.
2. Call the calculate_total_cost function of a ProcessChain, after any of its process steps is saved.
3. Create a script:
* Create a new ProcessChain.
* Create related 5 ProcessSteps (for-loop is allowed here) and assign a random cost values between 0.00 and 10.00. 
* Print the cost value for each ProcessStep after creating it.
* Print the total_cost of the ProcessChain.
* Assign the cost value of 100 to one of the process.
4. Create a repository and push the code.