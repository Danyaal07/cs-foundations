# Day 11 — Binary Tree Traversals (DFS)

## Topics
- Preorder Traversal
- Inorder Traversal
- Postorder Traversal
- Depth-First Search on Trees

---

## Question 1: Preorder Traversal (Root → Left → Right)

Given the root of a binary tree, return the preorder traversal of its node values.

You visit:
1. The current node
2. The left subtree
3. The right subtree

---

## Question 2: Inorder Traversal (Left → Root → Right)

Given the root of a binary tree, return the inorder traversal of its node values.

You visit:
1. The left subtree
2. The current node
3. The right subtree

Important fact:
- Inorder traversal of a Binary Search Tree gives a sorted list.

---

## Question 3: Postorder Traversal (Left → Right → Root)

Given the root of a binary tree, return the postorder traversal of its node values.

You visit:
1. The left subtree
2. The right subtree
3. The current node

Common use cases:
- Deleting trees
- Evaluating expression trees

---

## Input Used for All Questions
1
 \
  2
 /
3

---

## Key Insight

All three traversals use the same recursion pattern.  
The only difference is **when** the node value is processed.

---

## What I Learned
- DFS traversal order depends on when the node is visited
- Tree problems often reuse the same recursive structure
- Small changes in recursion placement create different behaviors

---

## Limitations
- Recursive solutions use O(h) stack space
- Deep trees can cause stack overflow
- Iterative versions are sometimes preferred in production