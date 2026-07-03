import camelot

tables = camelot.read_pdf('sample.pdf', pages='2', flavor='stream')
print(tables)
tables.export('output.csv', f='csv')  # Exports all tables to CSV
