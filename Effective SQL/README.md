# Effective SQL

## Chapter 1: Data Model Design
  * Item 1: Verify That All Tables Have a Primary Key
  * Item 2: Eliminate Redundant Storage of Data Items
  * Item 3: Get Rid of Repeating Groups
  * Item 4: Store Only One Property per Column
  * Item 5: Understand Why Storing Calculated Data Is Usually a Bad Idea 
  * Item 6: Define Foreign Keys to Protect Referential Integrity
  * Item 7: Be Sure Your Table Relationships Make Sense
  * Item 8: When 3NF Is Not Enough, Normalize More
  * Item 9: Use Denormalization for Information Warehouses
## Chapter 2: Programmability and Index Design
  * Item 10: Factor in Nulls When Creating Indexes
  * Item 11: Carefully Consider Creation of Indexes to Minimize Index and Data Scanning
  * Item 12: Use Indexes for More than Just Filtering
  * Item 13: Don't Go Overboard with Triggers
  * Item 14: Consider Using a Filtered Index to Include or Exclude a subset of Data
  * Item 15: Use Declarative Constraints Instead of Programming Checks
  * Item 16: Know Which SQL Dialect Your Product Uses and Write Accordingly
  * Item 17: Know When to Use Calculated Results in Indexes
## Chapter 3: When You Can't Change the Design
  * Item 18: Use Views to Simplify What Cannot Be Changed
  * Item 19: Use ETL to Turn Nonrelational Data into Information
  * Item 20: Create Summary Tables and Maintain Them
  * Item 21: Use UNION Statements to "Unpivot" Non-normalized Data
## Chapter 4: Filtering and Finding Data
  * Item 22: Understand Relational Algebra and How It Is Implemented in SQL
  * Item 23: Find Non-matches or Missing Records
  * Item 24: Know When to Use CASE to Solve a Problem
  * Item 25: Know Techniques to Solve Multiple-Criteria Problems
  * Item 26: Divide Your Data If You Need a Perfect Match
  * Item 27: Know How to Correctly Filter a Range of Dates on a Column
Containing Both Date and Time
  * Item 28: Write Sargable Queries to Ensure that the Engine Will Use Indexes
  * Item 29: Correctly Filter the "Right" Side of a "Left" Join
## Chapter 5: Aggregation
  * Item 30: Understand How GROUP BY Works
  * Item 31: Keep the GROUP BY Clause Small
  * Item 32: Leverage GROUP BY/HAVING to Solve Complex Problems 
  * Item 33: Find Maximum or Minimum Values   * Without Using GROUP BY 
  * Item 34: Avoid Getting an Erroneous COUNT() When Using OUTER JOIN 
  * Item 35: Include Zero-Value Rows When Testing for HAVING COUNT (x) < Some Number
  * Item 36: Use DISTINCT to Get Distinct Counts
  * Item 37: Know How to Use Window Functions
  * Item 38: Create Row Numbers and Rank a Row over Other Rows
  * Item 39: Create a Moving Aggregate
## Chapter 6: Subqueries
  * Item 40: Know Where You Can Use Subqueries
  * Item 41: Know the Difference between Correlated and Non-correlated Subqueries
  * Item 42: If possible, Use Common Table Expressions Instead of Subqueries 
  * Item 43: Create More Efficient Queries Using Joins Rather than Subqueries
## Chapter 7: Getting and Analyzing Metadata
  * Item 44: Learn to Use Your System's Query Analyzer
  * Item 45: Learn to Get Metadata about Your Database
  * Item 46: Understand How the Execution Plan Works
## Chapter 8: Cartesian Products
  * Item 47: Produce Combinations of Rows between Two Tables and Flag Rows in the Second That Indirectly Relate to the First
  * Item 48: Understand How to Rank Rows by Equal Quantiles
  * Item 49: Know How to Pair Rows in a Table with All Other Rows
  * Item 50: Understand How to List Categories and the Count of First, Second, or Third Preferences
## Chapter 9: Tally Tables
  * Item 51: Use a Tally Table to Generate Null Rows Based on a Parameter 
  * Item 52: Use a Tally Table and Window Functions for Sequencing
  * Item 53: Generate Multiple Rows Based on Range Values in a Tally Table
  * Item 54: Convert a Value in One Table Based on a Range of Values in a Tally Table
  * Item 55: Use a Date Table to Simplify Date Calculation
  * Item 56: Create an Appointment Calendar Table with All Dates Enumerated in a Range
  * Item 57: Pivot Data Using a Tally Table
## Chapter 10: Modeling Hierarchical Data
  * Item 58: Use an Adjacency List Model as the Starting Point
  * Item 59: Use Nested Sets for Fast Querying Performance with Infrequent Updates
  * Item 60: Use a Materialized Path for Simple Setup and Limited Searching 
  * Item 61: Use Ancestry Traversal Closure for Complex Searching

