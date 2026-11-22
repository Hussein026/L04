import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin():
    assert check_admin("") == False


# bug report 2
def test_r2_find_user():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    db.execute("INSERT INTO users VALUES ('alice')")
    assert find_user(db, "x' OR '1'='1") is None
