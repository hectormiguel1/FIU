|Contents|
----------
- [Query Optimization](#query-optimization)
  - [Implementation](#implementation)
  - [Equivalence Rules](#equivalence-rules)
  - [Video](#video)
# Query Optimization
## Implementation 
The query optimizer attempts to determine the most efficient way to execute a given query by considering query plans. 

Generally, the query optimizer cannot be accessed directly by the users; once the query are submitted the databse server, parsed by the user.... 

Most query optimizers represent query planms as a tree of 'plan nodes'. 

A plan node excapsulates a single operation that is required to execute the query.  The node arranged aas a tree, in which intermidate results flow from the bottom of the tree to the top. 

Each node has zero or mode child nodes - those are nodes whose output...


## Equivalence Rules
1. Conjunction selection can be deconstructed into a sequence of individual selections. 
2. Selection operations are commulattive. 
3. Only the last in a sequence of projection operations is needed, the others can be ommited. 
4. Selections be be combined with Cartesian Profucts and theta joins. 
   
## Video 
Start at Minutes 38 to minute 41
Move to minue 44 







