```
import sys

query = sys.argv[1]

output = query.lstrip().lstrip('>>> ').lstrip('... ').lstrip('    ')
sys.stdout.write(output)
```
