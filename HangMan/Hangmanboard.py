#! /usr/local/bin/python3

def board(): 
    print ("""
    +---+
    |
    |
    |
    |
    =======
    """)

def head():
    print ("""
    +---+
    |   O
    |
    |
    |
    =======
    You have 5 chances left. 
    """)

def body():
    print ("""
    +---+
    |   O
    |   |
    |
    |
    =======
    You have 4 chances left.
    """)

def rarm():
 print ("""
    +---+
    |   O
    |   |/
    |
    |
    =======
    You have 3 chances left. 
    """)

def larm():
    print ("""
    +---+
    |   O
    |  \\|/
    |
    |
    =======
    You have 2 chances left.
    """)

def lleg():
    print ("""
    +---+
    |   O
    |  \\|/
    |  /
    |
    =======
    Oh no, you have 1 chance left! 
    """)

def rleg():
    print ("""
    +---+
    |   O
    |  \|/
    |   /\\
    |
    =======
    You Lose!
    """)