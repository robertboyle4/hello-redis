
import re
import sys
from google.oauth2 import service_account
from google.auth.transport import requests
import base64
from pathlib import Path
import argparse
from typing import Optional
from typing import Sequence
import json
import os

def test(test1):
  test2 = os.environ.get("VAR_TEST", "Not Found")
  print("TEST1: $test1")
  print("TEST2: $test2")

def initialize_command_line_args(
    args: Optional[Sequence[str]] = None) -> Optional[argparse.Namespace]:
  """Initializes and checks all the command-line arguments."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "-v", "--var_test", type=str, help="Var test)")
    
  parser.set_defaults(make_changes=False)
  return parser.parse_args(args)

cli = initialize_command_line_args()
test(cli.var_test)
