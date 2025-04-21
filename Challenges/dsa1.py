# Algorithms and Data Structures in Python

# --- SEARCH ALGORITHMS ---

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- SORTING ALGORITHMS ---

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# --- STACK ---

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# --- QUEUE ---

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# --- LINKED LIST ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        return elems


# --- BINARY TREE ---

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")


# --- BREADTH-FIRST SEARCH (TREE) ---

from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# --- DEPTH-FIRST SEARCH (TREE) ---

def dfs(root):
    if root:
        print(root.value, end=" ")
        dfs(root.left)
        dfs(root.right)


# --- HASH TABLE / DICTIONARY EXAMPLE ---

def count_occurrences(arr):
    counter = {}
    for item in arr:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter


# --- SET OPERATIONS ---

def set_operations():
    a = set([1, 2, 3, 4])
    b = set([3, 4, 5, 6])
    return {
        "union": a | b,
        "intersection": a & b,
        "difference": a - b,
        "symmetric_difference": a ^ b
    }


# --- HEAP IMPLEMENTATION ---

import heapq

def heap_example():
    heap = []
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 2)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result


# --- TRIE (PREFIX TREE) ---

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# --- GRAPH (ADJACENCY LIST) ---

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.graph.get(vertex, []))

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in self.graph.get(vertex, []):
                self._dfs_recursive(neighbor, visited)
