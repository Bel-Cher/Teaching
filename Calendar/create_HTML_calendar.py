#!/usr/bin/python3

# Run as: create-html-table.py {input-file-name}
# The script requires 1 argument: the input file name.
# It expects a comma-separated input file to parse into an html table,
# and assumes that the column headers are located in the first row.

import sys

filein = open(sys.argv[1], "r")
fileout = open("html-table.html", "w")
data = filein.readlines()

table = '<table class="table table-bordered table-striped table-condensed" style="width: 109.082%;" width="289">\n'

# Create the table's column headers
header = data[0].split(";")
table += '  <thead>\n'
table += '      <tr>\n'
for column in header:
    table += "          <th>{0}</th>\n".format(column.strip())
table += "      </tr>\n"
table += "  </thead>\n"

# Create the table's row data
table += "  <tbody>\n"
for line in data[1:]:
    row = line.split(";")
    table += "      <tr>\n"
    for column in row:
        table += "        <td>{0}</td>\n".format(column.strip())
    table += "      </tr>\n"
table += "  </tbody>\n"
table += "</table>"

fileout.writelines(table)
fileout.close()
filein.close()