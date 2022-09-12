from deta import Deta
import pandas as pd
import streamlit as st

DETA_KEY = "c050exny_sE1wzsJo16sN4NJEq1uwxLkDa7kAZAxV"

deta = Deta(DETA_KEY)

db = deta.Base("result_reports")

def insert_db(record):
    return db.put(record)

