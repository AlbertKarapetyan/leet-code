# Merge Two Sorted Linked Lists

## Problem Statement

You are given the heads of two **sorted** linked lists, `list1` and `list2`.

Your task is to **merge** the two lists into a single sorted linked list. The resulting list should be created by **splicing together** the nodes from the original two lists.

Return the head of the **merged** linked list.

## Example

### Example 1  
**Input:**  
```
list1 = [1,2,4]
list2 = [1,3,4]
```
**Output:**  
```
[1,1,2,3,4,4]
```

### Example 2  
**Input:**  
```
list1 = []
list2 = []
```
**Output:**  
```
[]
```

### Example 3  
**Input:**  
```
list1 = []
list2 = [0]
```
**Output:**  
```
[0]
```

## Constraints  

- The number of nodes in both lists is in the range **[0, 50]**.  
- Each node value falls within the range **[-100, 100]**.  
- Both `list1` and `list2` are sorted in **non-decreasing order**.